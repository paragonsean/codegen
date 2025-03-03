#![allow(dead_code, mutable_transmutes, non_camel_case_types, non_snake_case,
         non_upper_case_globals, unused_assignments, unused_mut)]
#![register_tool(c2rust)]
#![feature(main, register_tool)]
extern "C" {
    #[no_mangle]
    fn printf(_: *const libc::c_char, _: ...) -> libc::c_int;
    #[no_mangle]
    fn qsort(__base: *mut libc::c_void, __nmemb: size_t, __size: size_t,
             __compar: __compar_fn_t);
}
pub type size_t = libc::c_ulong;
pub type __compar_fn_t
    =
    Option<unsafe extern "C" fn(_: *const libc::c_void,
                                _: *const libc::c_void) -> libc::c_int>;
// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//
#[no_mangle]
pub unsafe extern "C" fn min(mut x: libc::c_int, mut y: libc::c_int)
 -> libc::c_int {
    return if x < y { x } else { y };
}
#[no_mangle]
pub unsafe extern "C" fn max(mut x: libc::c_int, mut y: libc::c_int)
 -> libc::c_int {
    return if x > y { x } else { y };
}
#[no_mangle]
pub unsafe extern "C" fn cmpfunc(mut a: *const libc::c_void,
                                 mut b: *const libc::c_void) -> libc::c_int {
    return *(a as *mut libc::c_int) - *(b as *mut libc::c_int);
}
#[no_mangle]
pub unsafe extern "C" fn len(mut arr: *mut libc::c_int) -> libc::c_int {
    return (::std::mem::size_of::<*mut libc::c_int>() as
                libc::c_ulong).wrapping_div(::std::mem::size_of::<libc::c_int>()
                                                as libc::c_ulong) as
               libc::c_int;
}
#[no_mangle]
pub unsafe extern "C" fn sort(mut arr: *mut libc::c_int, mut n: libc::c_int) {
    qsort(arr as *mut libc::c_void, n as size_t,
          ::std::mem::size_of::<libc::c_int>() as libc::c_ulong,
          Some(cmpfunc as
                   unsafe extern "C" fn(_: *const libc::c_void,
                                        _: *const libc::c_void)
                       -> libc::c_int));
}
#[no_mangle]
pub unsafe extern "C" fn f_gold(mut m: libc::c_int, mut n: libc::c_int)
 -> libc::c_int {
    let vla = (n + 1 as libc::c_int) as usize;
    let mut factorCount: Vec<libc::c_longlong> =
        ::std::vec::from_elem(0, vla);
    let vla_0 = (n + 1 as libc::c_int) as usize;
    let mut prime: Vec<bool> = ::std::vec::from_elem(false, vla_0);
    let mut i: libc::c_int = 0 as libc::c_int;
    while i <= n {
        *factorCount.as_mut_ptr().offset(i as isize) =
            0 as libc::c_int as libc::c_longlong;
        *prime.as_mut_ptr().offset(i as isize) = 1 as libc::c_int != 0;
        i += 1
    }
    let mut i_0: libc::c_int = 2 as libc::c_int;
    while i_0 <= n {
        if *prime.as_mut_ptr().offset(i_0 as isize) as libc::c_int ==
               1 as libc::c_int {
            *factorCount.as_mut_ptr().offset(i_0 as isize) =
                1 as libc::c_int as libc::c_longlong;
            let mut j: libc::c_int = i_0 * 2 as libc::c_int;
            while j <= n {
                let ref mut fresh0 =
                    *factorCount.as_mut_ptr().offset(j as isize);
                *fresh0 += 1;
                *prime.as_mut_ptr().offset(j as isize) =
                    0 as libc::c_int != 0;
                j += i_0
            }
        }
        i_0 += 1
    }
    let mut max_0: libc::c_int =
        *factorCount.as_mut_ptr().offset(m as isize) as libc::c_int;
    let mut num: libc::c_int = m;
    let mut i_1: libc::c_int = m;
    while i_1 <= n {
        if *factorCount.as_mut_ptr().offset(i_1 as isize) >
               max_0 as libc::c_longlong {
            max_0 =
                *factorCount.as_mut_ptr().offset(i_1 as isize) as libc::c_int;
            num = i_1
        }
        i_1 += 1
    }
    return num;
}
#[no_mangle]
pub unsafe extern "C" fn f_filled(mut m: libc::c_int, mut n: libc::c_int)
 -> libc::c_int {
    panic!("Reached end of non-void function without returning");
}
unsafe fn main_0() -> libc::c_int {
    let mut n_success: libc::c_int = 0 as libc::c_int;
    let mut param0: [libc::c_int; 10] =
        [21 as libc::c_int, 92 as libc::c_int, 1 as libc::c_int,
         51 as libc::c_int, 97 as libc::c_int, 74 as libc::c_int,
         18 as libc::c_int, 45 as libc::c_int, 31 as libc::c_int,
         23 as libc::c_int];
    let mut param1: [libc::c_int; 10] =
        [6 as libc::c_int, 53 as libc::c_int, 60 as libc::c_int,
         85 as libc::c_int, 72 as libc::c_int, 17 as libc::c_int,
         37 as libc::c_int, 75 as libc::c_int, 47 as libc::c_int,
         87 as libc::c_int];
    let mut i: libc::c_int = 0 as libc::c_int;
    while i < len(param0.as_mut_ptr()) {
        if f_filled(param0[i as usize], param1[i as usize]) ==
               f_gold(param0[i as usize], param1[i as usize]) {
            n_success += 1 as libc::c_int
        }
        i += 1
    }
    printf(b"#Results:\x00" as *const u8 as *const libc::c_char,
           b" \x00" as *const u8 as *const libc::c_char, n_success,
           b", \x00" as *const u8 as *const libc::c_char,
           len(param0.as_mut_ptr()));
    return 0 as libc::c_int;
}
#[main]
pub fn main() { unsafe { ::std::process::exit(main_0() as i32) } }
