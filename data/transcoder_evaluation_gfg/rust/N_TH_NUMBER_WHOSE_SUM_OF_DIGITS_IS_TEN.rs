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

pub unsafe fn f_gold(mut n: i32) -> i32 {
    let mut count: i32 = 0 as i32;
    let mut curr: i32 = 1 as i32;
    loop  {
        let mut sum: i32 = 0 as i32;
        let mut x: i32 = curr;
        while x > 0 as i32 {
            sum = sum + x % 10 as i32;
            x = x / 10 as i32
        }
        if sum == 10 as i32 { count += 1 }
        if count == n { return curr }
        curr += 1
    };
}
//TOFILL
unsafe fn main_0() -> i32 {
    let mut n_success: i32 = 0 as i32;
    let mut param0: [i32; 10] =
        [37 as i32, 13 as i32, 51 as i32,
         69 as i32, 76 as i32, 10 as i32,
         97 as i32, 40 as i32, 69 as i32,
         4 as i32];
    let mut i: i32 = 0 as i32;
    while i < param0.len() as i32 {
        if f_filled(param0[i as usize]) == f_gold(param0[i as usize]) {
            n_success += 1 as i32
        }
        i += 1
    }
    println!("{} {} {} {} {}", "#Results:", " ", n_success, ", ", param0.len() as i32);
    return 0 as i32;
}
#[main]
pub fn main() { unsafe { ::std::process::exit(main_0() as i32) } }
