# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 fileencoding=utf-8
#
# MDAnalysis --- https://www.mdanalysis.org
# Copyright (c) 2006-2017 The MDAnalysis Development Team and contributors
# (see the file AUTHORS for the full list of names)
#
# Released under the GNU Public Licence, v2 or any higher version
#
# Please cite your use of MDAnalysis in published work:
#
# R. J. Gowers, M. Linke, J. Barnoud, T. J. E. Reddy, M. N. Melo, S. L. Seyler,
# D. L. Dotson, J. Domanski, S. Buchoux, I. M. Kenney, and O. Beckstein.
# MDAnalysis: A Python package for the rapid analysis of molecular dynamics
# simulations. In S. Benthall and S. Rostrup editors, Proceedings of the 15th
# Python in Science Conference, pages 102-109, Austin, TX, 2016. SciPy.
# doi: 10.25080/majora-629e541a-00e
#
# N. Michaud-Agrawal, E. J. Denning, T. B. Woolf, and O. Beckstein.
# MDAnalysis: A Toolkit for the Analysis of Molecular Dynamics Simulations.
# J. Comput. Chem. 32 (2011), 2319--2327, doi:10.1002/jcc.21787
#
import MDAnalysis as mda
import pytest
from MDAnalysis.analysis import nuclinfo
from MDAnalysisTests.datafiles import RNA_PSF, RNA_PDB, RNA_PDB2
from numpy.testing import (
    assert_almost_equal,
    assert_allclose,
)


@pytest.fixture(scope='module')
def u():
    return mda.Universe(RNA_PSF, RNA_PDB)


@pytest.fixture(scope='module')
def u2():
    return mda.Universe(RNA_PDB2)


@pytest.mark.parametrize('i, bp, seg1, seg2, expected_value', (
    ( 1,  2, 'RNAA', 'RNAA', 4.3874702),
    (22, 23, 'RNAA', 'RNAA', 4.1716404),
))
def test_wc_pair(u, i, bp, seg1, seg2, expected_value):
    val = nuclinfo.wc_pair(u, i, bp, seg1=seg1, seg2=seg2)
    assert_almost_equal(val, expected_value, decimal=3)


@pytest.mark.parametrize('i, bp, seg1, seg2, expected_value', (
    ( 3, 17, 'RNAA', 'RNAA', 15.06506),
    (20,  5, 'RNAA', 'RNAA', 3.219116),
))
def test_minor_pair(u, i, bp, seg1, seg2, expected_value):
    val = nuclinfo.minor_pair(u, i, bp, seg1=seg1, seg2=seg2)
    assert_almost_equal(val, expected_value, decimal=3)


@pytest.mark.parametrize('i, bp, seg1, seg2, expected_value', (
    (2, 12, 'RNAA', 'RNAA', 26.884272),
    (5,  9, 'RNAA', 'RNAA', 13.578535),
))
def test_major_pair(u, i, bp, seg1, seg2, expected_value):
    val = nuclinfo.major_pair(u, i, bp, seg1=seg1, seg2=seg2)
    assert_almost_equal(val, expected_value, decimal=3)


@pytest.mark.parametrize('seg, i, expected_value', (
    ('RNAA',  9,  3.16497),
    ('RNAA', 21, 22.07721),
))
def test_phase_cp(u, seg, i, expected_value):
    val = nuclinfo.phase_cp(u, seg=seg, i=i)
    assert_almost_equal(val, expected_value, decimal=3)


@pytest.mark.parametrize('seg, i, expected_value', (
    ('RNAA',  1, 359.57580),
    ('RNAA', 11, 171.71645),
))
def test_phase_as(u, seg, i, expected_value):
    val = nuclinfo.phase_as(u, seg=seg, i=i)
    assert_almost_equal(val, expected_value, decimal=3)


@pytest.mark.parametrize('seg, i, expected_value', (
    ('RNAA', 5, [302.203802, 179.043077,  35.271411,  79.499729, 201.000393,
                 282.14321 , 210.709327]),
    ('RNAA', 21, [280.388619, 185.12919 ,  56.616215,  64.87354 , 187.153367,
                  279.340915, 215.332144]),
))
def test_tors(u, seg, i, expected_value):
    val = nuclinfo.tors(u, seg=seg, i=i)
    assert_allclose(val, expected_value, rtol=1e-03)


@pytest.mark.parametrize('seg, i, expected_value', (
    ('RNAA',  6, 279.15103),
    ('RNAA', 18, 298.09936),
))
def test_tors_alpha(u, seg, i, expected_value):
    val = nuclinfo.tors_alpha(u, seg=seg, i=i)
    assert_almost_equal(val, expected_value, decimal=3)


@pytest.mark.parametrize('seg, i, expected_value', (
    ('RNAA',  7, 184.20501),
    ('RNAA', 15, 169.70042),
))
def test_tors_beta(u, seg, i, expected_value):
    val = nuclinfo.tors_beta(u, seg=seg, i=i)
    assert_almost_equal(val, expected_value, decimal=3)


@pytest.mark.parametrize('seg, i, expected_value', (
    ('RNAA',  7, 52.72022),
    ('RNAA', 15, 54.59684),
))
def test_tors_gamma(u, seg, i, expected_value):
    val = nuclinfo.tors_gamma(u, seg=seg, i=i)
    assert_almost_equal(val, expected_value, decimal=3)


@pytest.mark.parametrize('seg, i, expected_value', (
    ('RNAA',  7, 84.80554),
    ('RNAA', 15, 82.00043),
))
def test_tors_delta(u, seg, i, expected_value):
    val = nuclinfo.tors_delta(u, seg=seg, i=i)
    assert_almost_equal(val, expected_value, decimal=3)


@pytest.mark.parametrize('seg, i, expected_value', (
    ('RNAA',  7, 200.40990),
    ('RNAA', 15, 210.96953),
))
def test_tors_eps(u, seg, i, expected_value):
    val = nuclinfo.tors_eps(u, seg=seg, i=i)
    assert_almost_equal(val, expected_value, decimal=3)


@pytest.mark.parametrize('seg, i, expected_value', (
        ('RNAA',  7, 297.84736),
        ('RNAA', 15, 330.24898)
))
def test_tors_zeta(u, seg, i, expected_value):
    val = nuclinfo.tors_zeta(u, seg=seg, i=i)
    assert_almost_equal(val, expected_value, decimal=3)


@pytest.mark.parametrize('seg, i, expected_value', (
        ('RNAA',  1, 178.37435),
        ('RNAA',  2, 202.03418),
        ('RNAA',  7, 200.91674),
        ('RNAA', 15, 209.32109),
))
def test_tors_chi(u, seg, i, expected_value):
    val = nuclinfo.tors_chi(u, seg=seg, i=i)
    assert_almost_equal(val, expected_value, decimal=3)


@pytest.mark.parametrize('seg, i, expected_value', (
        ('RNAA', 20, 103.07024),
        ('RNAA',  5, 156.62223),
        ('RNAA',  7 , 77.94538),
        ('RNAA', 15, 130.18539),
))
def test_hydroxyl(u, seg, i, expected_value):
    val = nuclinfo.hydroxyl(u, seg=seg, i=i)
    assert_almost_equal(val, expected_value, decimal=3)


@pytest.mark.parametrize('bp1, bp2, i, seg1, seg2, seg3, expected_value', (
        (16, 2, 3, 'RNAA', 'RNAA', 'RNAA', 314.69804),
        (8, 9, 10, 'RNAA', 'RNAA', 'RNAA', 34.50106),
))
def test_pseudo_dihe_baseflip(u, bp1, bp2, i, seg1, seg2, seg3, expected_value):
    val = nuclinfo.pseudo_dihe_baseflip(u, bp1, bp2, i, seg1, seg2, seg3)
    assert_almost_equal(val, expected_value, decimal=3)


@pytest.mark.parametrize('b1, b2, seg1, seg2, expected_value', (
        (2, 3, 'RNAA', 'RNAA', 15.490582),
        (10, 11, 'RNAA', 'RNAA', 43.71941),
        (7, 17, 'RNAA', 'RNAA', 168.37481),
))
def test_angle_between_base_planes(u, b1, b2, seg1, seg2, expected_value):
    val = nuclinfo.angle_between_base_planes(u, b1, b2, seg1, seg2)
    assert_allclose(val, expected_value, rtol=1e-3, atol=0)


def test_warn1_angle_between_base_plane(u2):
    sele = u2.select_atoms('resid 3')
    res, segid = sele.residues.resids[0], sele.segments.segids[0]
    errmsg = (f"Found more than one residues with resid {res} and "
              f"segid {segid}. Using first residue in selection.")
    with pytest.warns(UserWarning, match=errmsg):
        b1, b2 = 3, 4
        ANGL = nuclinfo.angle_between_base_planes(u2, b1, b2)


def test_KeyError_angle_between_base_plane(u2):
    errmsg = ("Residue names may be incorrect! "
              "Please use either ADE/GUA/CYT/URA/THY or A/G/C/U/T format.")
    with pytest.raises(KeyError, match=errmsg):
        b1, b2 = 9, 10
        ANGL = nuclinfo.angle_between_base_planes(u2, b1, b2)


def test_IndexError_angle_between_base_plane(u2):
    errmsg = ("Atom names may be incorrect! "
              "Make sure base atom names follow CHARMM format.")
    with pytest.raises(IndexError, match=errmsg):
        b1, b2 = 11, 12
        ANGL = nuclinfo.angle_between_base_planes(u2, b1, b2)


def test_warn2_angle_between_base_plane(u2):
    errmsg = ("No box information found!"
              "Calculation will continue by ignoring PBC.")
    with pytest.warns(UserWarning, match=errmsg):
        b1, b2 = 1, 2
        ANGL = nuclinfo.angle_between_base_planes(u2, b1, b2)
