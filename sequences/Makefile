# build:
# 	g++ -Wall -Weffc++ -pedantic -pedantic-errors -Wextra -Wcast-align -Wcast-qual -Wconversion -Wdisabled-optimization -Wfloat-equal -Wformat=2 -Wformat-nonliteral -Wformat-security -Wformat-y2k -Wimport  -Winit-self  -Winline -Winvalid-pch  -Wmissing-field-initializers -Wmissing-format-attribute  -Wmissing-include-dirs -Wmissing-noreturn -Wno-sign-conversion -Wpacked  -Wpointer-arith -Wredundant-decls -Wshadow -Wstack-protector -Wstrict-aliasing=2 -Wswitch-default -Wswitch-enum -Wunreachable-code -Wunused -Wunused-but-set-variable -Wunused-parameter -Wvariadic-macros -Wwrite-strings *.h *.cpp -g 
# build:
# 	g++ -g -fsanitize=address -fsanitize=undefined -D_GLIBCXX_DEBUG -g *.cpp *.h -w
nw_rw:
	icc nw_rw.cpp align.cpp helper.cpp -g -O0 -o nw_rw
#	g++ -g -O0 *.cpp
nw_rw_opt:
	icc nw_rw.cpp align.cpp helper.cpp -g -O3 -qopenmp -axCORE-AVX2 -o nw_rw_opt
nw_ad:
	icc nw_ad.cpp align_optimise.cpp helper.cpp -g -O3 -qopenmp -axCORE-AVX2 -o nw_ad
nw_tile_50:
	icc nw_tile_50.cpp align_tile.cpp helper.cpp -g -O3 -qopenmp -axCORE-AVX2 -o nw_tile_50
nw_tile_100:
	icc nw_tile_100.cpp align_tile.cpp helper.cpp -g -O3 -qopenmp -axCORE-AVX2 -o nw_tile_100
nw_tile_200:
	icc nw_tile_200.cpp align_tile.cpp helper.cpp -g -O3 -qopenmp -axCORE-AVX2 -o nw_tile_200
nw_tile_500:
	icc nw_tile_500.cpp align_tile.cpp helper.cpp -g -O3 -qopenmp -axCORE-AVX2 -o nw_tile_500
nw_tile_1000:
	icc nw_tile_1000.cpp align_tile.cpp helper.cpp -g -O3 -qopenmp -axCORE-AVX2 -o nw_tile_1000
