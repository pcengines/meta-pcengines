DEFAULTTUNE ?= "dbft3b"

require conf/machine/include/x86/arch-x86.inc
require conf/machine/include/x86/x86-base.inc

# AMD DB-FT3b 64bit (SteppeEagle)
TUNEVALID[dbft3b] = "Enable AMD DB-FT3b (64 bit) specific processor optimizations"
TUNECONFLICTS[dbft3b] = "m32 mx32"
TUNE_CCARGS .= "${@bb.utils.contains("TUNE_FEATURES", "dbft3b", " -march=btver2", "", d)}"

# Extra tune selections
AVAILTUNES += "dbft3b"
TUNE_FEATURES:tune-dbft3b = "m64 dbft3b"
BASE_LIB:tune-dbft3b = "lib64"
TUNE_PKGARCH:tune-dbft3b = "dbft3b"
PACKAGE_EXTRA_ARCHS:tune-dbft3b = "${TUNE_PKGARCH:tune-dbft3b}"
