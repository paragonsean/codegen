/*
 * This file was automatically generated by EvoSuite
 * Wed Apr 21 13:17:21 GMT 2021
 */


import org.junit.Test;
import static org.junit.Assert.*;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true, separateClassLoader = true) 
public class CLASS_4819651a89a417bce7b2158d1101004f26892e6022f6d1e6348175e23666ec38_ESTest extends CLASS_4819651a89a417bce7b2158d1101004f26892e6022f6d1e6348175e23666ec38_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Double double0 = new Double(3051.0);
      double double1 = CLASS_4819651a89a417bce7b2158d1101004f26892e6022f6d1e6348175e23666ec38.simplep(double0);
      assertEquals(3051.0, double1, 1.0E-4);
  }