#pragma once

#ifdef _MSC_VER
/* link to SDL and dependent windows libraries */
#   pragma comment(lib, "imm32.lib")
#   pragma comment(lib, "version.lib")
#   pragma comment(lib, "winmm.lib")
#   pragma comment(lib, "SDL2.lib")
#   pragma comment(lib, "SDL2main.lib")
#endif