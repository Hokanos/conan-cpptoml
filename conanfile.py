from conans import ConanFile, CMake, tools
import os

class CpptomlConan(ConanFile):
    name = "cpptoml"
    version = "0.4.0-2051836"
    license = "MIT"
    url = "git@github.com:Hokanos/conan-cpptoml.git"
    description = "toml parser"
    settings = None
    generators = "cmake"

    GIT_SOURCE = "https://github.com/skystrife/cpptoml.git"
    GIT_HASH = "2051836a96a25e5a2d5283be7f633a157848f15e"

    def source(self):
        self.run("git clone " + self.GIT_SOURCE)

        with tools.chdir("cpptoml"):
            self.run("git checkout " + self.GIT_HASH)

    def build(self):
        pass

    def package(self):
        self.copy("*.h", dst="include", src=os.path.join("cpptoml", "include"))

    def package_info(self):
        self.cpp_info.includedirs = ['include']
