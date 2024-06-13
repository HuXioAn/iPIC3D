# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install testspack
#
# You can edit this file again by typing:
#
#     spack edit testspack
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Testspack(CMakePackage):
    """ iPIC3D
        An implicit PIC simulator for plasma physics...
    """

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/HuXioAn/iPIC3D"
    url = "https://github.com/HuXioAn/iPIC3D/archive/refs/tags/trv1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers("hu7006@outlook.com")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    #license("UNKNOWN", checked_by="github_user1")

    version("1", sha256="d1ed7b4d53938075b01480d77ec4f02960b5ef9cf865423e6a9d2b87a70c5ad3")

    # FIXME: Add dependencies if required.
    depends_on("mpich")
    depends_on("hdf5")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = ["-DCMAKE_BUILD_TYPE=Debug"]
        return args