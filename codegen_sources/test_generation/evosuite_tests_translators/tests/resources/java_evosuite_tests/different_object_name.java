/*
 * This file was automatically generated by EvoSuite
 * Fri Jun 18 14:55:38 GMT 2021
 */


import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true, separateClassLoader = true)
public class CLASS_FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES_2_ESTest extends CLASS_FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES_2_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      CLASS_FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES_2 cLASS_FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES_2_0 = new CLASS_FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES_2();
      int[] intArray0 = new int[1];
      int int0 = cLASS_FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES_2_0.getOddOccurrence(intArray0, (-39131));
      assertEquals(0, int0);
  }
}