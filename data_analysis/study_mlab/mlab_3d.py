#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/24 21:32
# @Author  : Tom.lee
# @Site    : 
# @File    : mlab_a.py
# @Software: PyCharm


def surface_3d():
    """
    使用Mayavi将二维数组绘制成3D曲面 x * exp(x**2 - y**2)
    :return:
    """
    import numpy as np
    # create data
    x, y = np.ogrid[-2:2:20j, -2:2:20j]
    z = x * np.exp(- x ** 2 - y ** 2)

    # view it
    from mayavi import mlab

    # 绘制一个三维空间中的曲面
    pl = mlab.surf(x, y, z, warp_scale="auto")

    # 在三维空间中添加坐标轴
    mlab.axes(xlabel='x', ylabel='y', zlabel='z')

    # 在三维空间中添加曲面区域的外框
    mlab.outline(pl)

    mlab.show()


def surface_spherical_harmonic():
    # Create the data.
    from numpy import pi, sin, cos, mgrid
    dphi, dtheta = pi / 250.0, pi / 250.0
    [phi, theta] = mgrid[0:pi + dphi * 1.5:dphi, 0:2 * pi + dtheta * 1.5:dtheta]
    m0 = 4
    m1 = 3
    m2 = 2
    m3 = 3
    m4 = 6
    m5 = 2
    m6 = 6
    m7 = 4
    r = sin(m0 * phi) ** m1 + cos(m2 * phi) ** m3 + sin(m4 * theta) ** m5 + cos(m6 * theta) ** m7
    x = r * sin(phi) * cos(theta)
    y = r * cos(phi)
    z = r * sin(phi) * sin(theta)

    # View it.
    from mayavi import mlab
    mlab.mesh(x, y, z)
    mlab.show()


def test_plot3d():
    import numpy
    from mayavi import mlab

    """Generates a pretty set of lines."""
    n_mer, n_long = 6, 11
    pi = numpy.pi
    dphi = pi / 1000.0
    phi = numpy.arange(0.0, 2 * pi + 0.5 * dphi, dphi)
    mu = phi * n_mer
    x = numpy.cos(mu) * (1 + numpy.cos(n_long * mu / n_mer) * 0.5)
    y = numpy.sin(mu) * (1 + numpy.cos(n_long * mu / n_mer) * 0.5)
    z = numpy.sin(n_long * mu / n_mer) * 0.5

    l = mlab.plot3d(x, y, z, numpy.sin(mu), tube_radius=0.025, colormap='Spectral')
    mlab.show()


if __name__ == '__main__':
    # surface_spherical_harmonic()
    # surface_3d()
    test_plot3d()
