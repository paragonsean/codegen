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
    #[no_mangle]
    fn memset(_: *mut libc::c_void, _: libc::c_int, _: libc::c_ulong)
     -> *mut libc::c_void;
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
pub unsafe extern "C" fn f_gold(mut n: libc::c_int, mut r: libc::c_int,
                                mut p: libc::c_int) -> libc::c_int {
    let vla = (r + 1 as libc::c_int) as usize;
    let mut C: Vec<libc::c_int> = ::std::vec::from_elem(0, vla);
    memset(C.as_mut_ptr() as *mut libc::c_void, 0 as libc::c_int,
           (vla * ::std::mem::size_of::<libc::c_int>()) as libc::c_ulong);
    *C.as_mut_ptr().offset(0 as libc::c_int as isize) = 1 as libc::c_int;
    let mut i: libc::c_int = 1 as libc::c_int;
    while i <= n {
        let mut j: libc::c_int = min(i, r);
        while j > 0 as libc::c_int {
            *C.as_mut_ptr().offset(j as isize) =
                (*C.as_mut_ptr().offset(j as isize) +
                     *C.as_mut_ptr().offset((j - 1 as libc::c_int) as isize))
                    % p;
            j -= 1
        }
        i += 1
    }
    return *C.as_mut_ptr().offset(r as isize);
}
#[no_mangle]
pub unsafe extern "C" fn f_filled(mut n: libc::c_int, mut r: libc::c_int,
                                  mut p: libc::c_int) -> libc::c_int {
    panic!("Reached end of non-void function without returning");
}
unsafe fn main_0() -> libc::c_int {
    let mut n_success: libc::c_int = 0 as libc::c_int;
    let mut param0: [libc::c_int; 10] =
        [82 as libc::c_int, 45 as libc::c_int, 44 as libc::c_int,
         88 as libc::c_int, 90 as libc::c_int, 98 as libc::c_int,
         80 as libc::c_int, 60 as libc::c_int, 52 as libc::c_int,
         71 as libc::c_int];
    let mut param1: [libc::c_int; 10] =
        [5 as libc::c_int, 24 as libc::c_int, 68 as libc::c_int,
         24 as libc::c_int, 75 as libc::c_int, 55 as libc::c_int,
         54 as libc::c_int, 75 as libc::c_int, 73 as libc::c_int,
         26 as libc::c_int];
    let mut param2: [libc::c_int; 10] =
        [94 as libc::c_int, 95 as libc::c_int, 61 as libc::c_int,
         43 as libc::c_int, 57 as libc::c_int, 43 as libc::c_int,
         88 as libc::c_int, 65 as libc::c_int, 86 as libc::c_int,
         45 as libc::c_int];
    let mut i: libc::c_int = 0 as libc::c_int;
    while i < len(param0.as_mut_ptr()) {
        if f_filled(param0[i as usize], param1[i as usize],
                    param2[i as usize]) ==
               f_gold(param0[i as usize], param1[i as usize],
                      param2[i as usize]) {
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
