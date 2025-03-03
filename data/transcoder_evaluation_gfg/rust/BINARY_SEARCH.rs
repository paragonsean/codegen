#![feature(main)]
// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

#[no_mangle]
pub unsafe fn abs(mut x: i32)
 -> i32 {
    return x.abs();
}

#[no_mangle]
pub unsafe fn min(mut x: i32, mut y: i32)
 -> i32 {
    return if x < y { x } else { y };
}
#[no_mangle]
pub unsafe fn max(mut x: i32, mut y: i32)
 -> i32 {
    return if x > y { x } else { y };
}

pub unsafe fn f_gold(mut arr: *mut i32, mut l: i32,
                                mut r: i32, mut x: i32)
 -> i32 {
    if r >= l {
        let mut mid: i32 = l + (r - l) / 2 as i32;
        if *arr.offset(mid as isize) == x { return mid }
        if *arr.offset(mid as isize) > x {
            return f_gold(arr, l, mid - 1 as i32, x)
        }
        return f_gold(arr, mid + 1 as i32, r, x)
    }
    return -(1 as i32);
}
//TOFILL
unsafe fn main_0() -> i32 {
    let mut n_success: i32 = 0 as i32;
    let mut param0_0: [i32; 24] =
        [3 as i32, 4 as i32, 4 as i32,
         8 as i32, 9 as i32, 13 as i32,
         13 as i32, 15 as i32, 18 as i32,
         27 as i32, 30 as i32, 32 as i32,
         42 as i32, 48 as i32, 50 as i32,
         52 as i32, 56 as i32, 66 as i32,
         69 as i32, 69 as i32, 77 as i32,
         84 as i32, 84 as i32, 93 as i32];
    let mut param0_1: [i32; 45] =
        [52 as i32, -(58 as i32), -(22 as i32),
         -(80 as i32), 44 as i32, -(52 as i32),
         -(34 as i32), 94 as i32, -(34 as i32),
         -(74 as i32), 42 as i32, 60 as i32,
         -(62 as i32), 70 as i32, 98 as i32,
         32 as i32, 10 as i32, 94 as i32,
         26 as i32, 56 as i32, -(48 as i32),
         -(50 as i32), 42 as i32, 2 as i32,
         46 as i32, 28 as i32, -(68 as i32),
         -(16 as i32), -(96 as i32), -(12 as i32),
         66 as i32, -(46 as i32), 74 as i32,
         -(60 as i32), -(52 as i32), 28 as i32,
         -(92 as i32), -(78 as i32), 32 as i32,
         28 as i32, 16 as i32, 34 as i32,
         30 as i32, -(60 as i32), -(14 as i32)];
    let mut param0_2: [i32; 2] = [0 as i32, 1 as i32];
    let mut param0_3: [i32; 4] =
        [28 as i32, 84 as i32, 40 as i32,
         81 as i32];
    let mut param0_4: [i32; 12] =
        [-(66 as i32), -(62 as i32), -(60 as i32),
         -(56 as i32), -(56 as i32), -(2 as i32),
         40 as i32, 44 as i32, 50 as i32,
         74 as i32, 82 as i32, 94 as i32];
    let mut param0_5: [i32; 11] =
        [1 as i32, 0 as i32, 0 as i32,
         0 as i32, 0 as i32, 1 as i32,
         0 as i32, 1 as i32, 0 as i32,
         1 as i32, 1 as i32];
    let mut param0_6: [i32; 12] =
        [15 as i32, 26 as i32, 31 as i32,
         36 as i32, 36 as i32, 61 as i32,
         68 as i32, 72 as i32, 75 as i32,
         79 as i32, 82 as i32, 98 as i32];
    let mut param0_7: [i32; 46] =
        [0 as i32, -(82 as i32), -(94 as i32),
         48 as i32, 48 as i32, -(96 as i32),
         14 as i32, 66 as i32, 76 as i32,
         -(30 as i32), 86 as i32, 28 as i32,
         -(28 as i32), -(66 as i32), -(64 as i32),
         92 as i32, -(94 as i32), -(66 as i32),
         86 as i32, 26 as i32, 8 as i32,
         94 as i32, -(82 as i32), -(80 as i32),
         4 as i32, -(26 as i32), 76 as i32,
         -(46 as i32), 72 as i32, 88 as i32,
         -(6 as i32), 8 as i32, -(30 as i32),
         40 as i32, -(88 as i32), 2 as i32,
         -(40 as i32), -(98 as i32), -(22 as i32),
         -(20 as i32), 4 as i32, -(12 as i32),
         54 as i32, -(20 as i32), -(36 as i32),
         12 as i32];
    let mut param0_8: [i32; 13] =
        [0 as i32, 0 as i32, 0 as i32,
         0 as i32, 0 as i32, 0 as i32,
         0 as i32, 1 as i32, 1 as i32,
         1 as i32, 1 as i32, 1 as i32,
         1 as i32];
    let mut param0_9: [i32; 2] =
        [81 as i32, 47 as i32];
    let mut param0: [*mut i32; 10] =
        [param0_0.as_mut_ptr(), param0_1.as_mut_ptr(), param0_2.as_mut_ptr(),
         param0_3.as_mut_ptr(), param0_4.as_mut_ptr(), param0_5.as_mut_ptr(),
         param0_6.as_mut_ptr(), param0_7.as_mut_ptr(), param0_8.as_mut_ptr(),
         param0_9.as_mut_ptr()];
    let mut param1: [i32; 10] =
        [19 as i32, 40 as i32, 1 as i32,
         2 as i32, 8 as i32, 7 as i32,
         6 as i32, 38 as i32, 12 as i32,
         1 as i32];
    let mut param2: [i32; 10] =
        [12 as i32, 35 as i32, 1 as i32,
         2 as i32, 6 as i32, 7 as i32,
         7 as i32, 33 as i32, 10 as i32,
         1 as i32];
    let mut param3: [i32; 10] =
        [22 as i32, 44 as i32, 1 as i32,
         2 as i32, 8 as i32, 10 as i32,
         8 as i32, 39 as i32, 6 as i32,
         1 as i32];
    let mut i: i32 = 0 as i32;
    while i < param0.len() as i32 {
        if f_filled(param0[i as usize], param1[i as usize],
                    param2[i as usize], param3[i as usize]) ==
               f_gold(param0[i as usize], param1[i as usize],
                      param2[i as usize], param3[i as usize]) {
            n_success += 1 as i32
        }
        i += 1
    }
    println!("{} {} {} {} {}", "#Results:", " ", n_success, ", ", param0.len() as i32);
    return 0 as i32;
}
#[main]
pub fn main() { unsafe { ::std::process::exit(main_0() as i32) } }
