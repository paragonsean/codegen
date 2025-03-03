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
    fn abs(_: libc::c_int) -> libc::c_int;
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
pub unsafe extern "C" fn f_gold(mut a: libc::c_double, mut b: libc::c_double)
 -> libc::c_double {
    let mut mod_0: libc::c_double = 0.;
    if a < 0 as libc::c_int as libc::c_double {
        mod_0 = -a
    } else { mod_0 = a }
    if b < 0 as libc::c_int as libc::c_double { b = -b }
    while mod_0 >= b { mod_0 = mod_0 - b }
    if a < 0 as libc::c_int as libc::c_double { return -mod_0 }
    return mod_0;
}
#[no_mangle]
pub unsafe extern "C" fn f_filled(mut a: libc::c_double,
                                  mut b: libc::c_double) -> libc::c_double {
    panic!("Reached end of non-void function without returning");
}
unsafe fn main_0() -> libc::c_int {
    let mut n_success: libc::c_int = 0 as libc::c_int;
    let mut param0: [libc::c_double; 10] =
        [3243.229719038493f64, -4362.665881044217f64, 7255.066257575837f64,
         -6929.554320261099f64, 3569.942027998315f64, -6513.849053096595f64,
         7333.183189243961f64, -2856.1752826258803f64, 9787.228111241662f64,
         -1722.873699288031f64];
    let mut param1: [libc::c_double; 10] =
        [5659.926861939672f64, -9196.507113304497f64, 2623.200060506935f64,
         -3009.0234530313287f64, 6920.809419868375f64, -70.95992406437102f64,
         580.3500610971768f64, -9625.97442825802f64, 2419.6844962423256f64,
         -8370.700544254058f64];
    let mut i: libc::c_int = 0 as libc::c_int;
    while i < len(param0.as_mut_ptr() as *mut libc::c_int) {
        if (abs((1 as libc::c_int as libc::c_double -
                     (0.0000001f64 +
                          abs(f_gold(param0[i as usize], param1[i as usize])
                                  as libc::c_int) as libc::c_double) /
                         (abs(f_filled(param0[i as usize], param1[i as usize])
                                  as libc::c_int) as libc::c_double +
                              0.0000001f64)) as libc::c_int) as
                libc::c_double) < 0.001f64 {
            n_success += 1 as libc::c_int
        }
        i += 1
    }
    printf(b"#Results:\x00" as *const u8 as *const libc::c_char,
           b" \x00" as *const u8 as *const libc::c_char, n_success,
           b", \x00" as *const u8 as *const libc::c_char,
           len(param0.as_mut_ptr() as *mut libc::c_int));
    return 0 as libc::c_int;
}
#[main]
pub fn main() { unsafe { ::std::process::exit(main_0() as i32) } }
