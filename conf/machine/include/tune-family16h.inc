DEFAULTTUNE ?= "family16h"

require conf/machine/include/x86/arch-x86.inc
require conf/machine/include/x86-base.inc

# CPUs based on AMD Family 16h cores with x86-64 instruction set support. This
# includes MOVBE, F16C, BMI, AVX, PCL_MUL, AES, SSE4.2, SSE4.1, CX16, ABM,
# SSE4A, SSSE3, SSE3, SSE2, SSE, MMX and 64-bit instruction set extensions.
TUNEVALID[family16h] = "Enable AMD Family 16h (64 bit) specific processor optimizations"
TUNECONFLICTS[family16h] = "m32 mx32"
TUNE_CCARGS .= "${@bb.utils.contains("TUNE_FEATURES", "family16h", " -march=btver2", "", d)}"

# Extra tune selections
AVAILTUNES += "family16h"
TUNE_FEATURES_tune-family16h = "m64 family16h"
BASE_LIB_tune-family16h = "lib64"
TUNE_PKGARCH_tune-family16h = "family16h"
PACKAGE_EXTRA_ARCHS_tune-family16h = "${TUNE_PKGARCH_tune-family16h}"
