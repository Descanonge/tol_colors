"""Test all module."""

import os

import matplotlib.pyplot as plt
import pytest
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

import tol_colors as tc


class TestColorsets:
    csets_type = dict(
        bright=tc.Bright,
        vibrant=tc.Vibrant,
        muted=tc.Muted,
        high_contrast=tc.HighContrast,
        medium_contrast=tc.MediumContrast,
        pale=tc.Pale,
        dark=tc.Dark,
        light=tc.Light,
        land_cover=tc.LandCover,
    )

    def test_attributes(self):
        for name, t in self.csets_type.items():
            assert isinstance(getattr(tc, name), t)

    def test_mapping(self):
        assert len(tc.colorsets) == len(self.csets_type)

        for name, t in self.csets_type.items():
            assert isinstance(tc.colorsets[name], t)

        # test hyphens management
        assert tc.colorsets["high_contrast"] == tc.colorsets["high-contrast"]
        assert tc.colorsets["medium_contrast"] == tc.colorsets["medium-contrast"]
        assert tc.colorsets["land_cover"] == tc.colorsets["land-cover"]

    def test_values(self):
        # only test some of the values
        assert tc.bright.blue == "#4477AA"
        assert tc.vibrant.magenta == "#EE3377"
        assert tc.muted.sand == "#DDCC77"
        assert tc.high_contrast.yellow == "#DDAA33"
        assert tc.medium_contrast.light_red == "#EE99AA"
        assert tc.pale.pale_red == "#FFCCCC"
        assert tc.light.pink == "#FFAABB"
        assert tc.dark.dark_green == "#225522"
        assert tc.land_cover.mixed_forest == "#55AA22"

    def test_set_default(self, capfd, tmp_path):
        def config_line(cset):
            colors = [f"'{c[1:]}'" for c in tc.colorsets[cset]]
            line = f"axes.prop_cycle : cycler('color', [{', '.join(colors)}])"
            return line

        target_bright = (
            "axes.prop_cycle : cycler('color', ['4477AA', 'EE6677', '228833', "
            "'CCBB44', '66CCEE', 'AA3377', 'BBBBBB'])"
        )
        assert config_line("bright") == target_bright

        # Test dry-run
        fname = tmp_path / "matplotlibrc"
        tc.set_default_colors("bright", fname=fname, dry=True)
        assert not os.path.exists(fname)
        captured = capfd.readouterr()
        assert captured.out.splitlines()[-1] == "New config line: " + target_bright

        # Test writing to file
        tc.set_default_colors("bright", fname=fname)
        with open(fname) as fd:
            lines = fd.readlines()
            assert len(lines) == 1
            assert lines[0] == target_bright + "\n"

        # Test changing existing file (only one line in file)
        tc.set_default_colors("vibrant", fname=fname)
        with open(fname) as fd:
            lines = fd.readlines()
            assert len(lines) == 1
            assert lines[0] == config_line("vibrant") + "\n"

        # changing existing file (multiple lines)
        lines += ["\n", "font.size : 9\n"]
        with open(fname, "w") as fd:
            fd.writelines(lines)
        tc.set_default_colors("pale", fname=fname)
        with open(fname) as fd:
            lines = fd.readlines()
            assert lines == [config_line("pale") + "\n", "\n", "font.size : 9\n"]


class TestColormaps:
    cmaps_discrete = ["sunset", "BuRd", "PRGn", "YlOrBr", "WhOrBr"]
    cmaps_linear = [
        "iridescent",
        "rainbow",
        "rainbow_WhBr",
        "rainbow_WhRd",
        "rainbow_PuRd",
        "rainbow_PuBr",
    ]

    def get_linear(self):
        yield from self.cmaps_discrete + self.cmaps_linear
        yield from [f"{name}_r" for name in self.cmaps_discrete + self.cmaps_linear]

    def get_discrete(self):
        discrete = [f"{name}_discrete" for name in self.cmaps_discrete]
        yield from discrete
        yield from [f"{name}_r" for name in discrete]

    def get_all(self):
        yield from self.get_linear()
        yield from self.get_discrete()

    def test_attributes(self):
        for name in self.get_all():
            assert hasattr(tc, name)

    def test_mapping(self):
        for name in self.get_all():
            assert name in tc.colormaps

        all_names = list(self.get_all())
        assert len(all_names) == len(tc.colormaps)

    def test_types(self):
        for name in self.get_linear():
            assert isinstance(tc.colormaps[name], LinearSegmentedColormap)
            assert isinstance(getattr(tc, name), LinearSegmentedColormap)
        for name in self.get_discrete():
            assert isinstance(tc.colormaps[name], ListedColormap)
            assert isinstance(getattr(tc, name), ListedColormap)

    def test_registered(self):
        for name in self.get_all():
            assert f"tol.{name}" in plt.colormaps

    def test_discrete_rainbow(self):
        for i in range(1, 24):
            cmap = tc.rainbow_discrete(i)
            assert isinstance(cmap, ListedColormap)
            assert cmap.N == i

        for i in [0, 25]:
            with pytest.raises(ValueError):
                tc.rainbow_discrete(i)
