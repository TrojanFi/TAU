import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;
import static org.junit.Assert.assertArrayEquals;

public class MathTest {

    private Math math;

    @Before
    public void setMath(){
        math = new Math();
        System.out.println("Before");
    }

    @After
    public void tearMath(){
        math = null;
        System.out.println("After");
    }

    @Test
    public void dividing01() {
        int result = math.dividing(1,2,3);
        assertEquals(0,result);
        System.out.println("Test dividing01");
    }

    @Test
    public void dividing02() {
        int result = math.dividing(3,2,1);
        assertEquals(1,result);
        System.out.println("Test dividing02");
    }

    @Test
    public void dividing03() {
        int result = math.dividing(0,2,1);
        assertEquals(0,result);
        System.out.println("Test dividing03");
    }

    @Test
    public void dividing04() {
        int result = math.dividing(2,2,0);
        assertEquals(0,result);
        System.out.println("Test dividing04");
    }

    @Test
    public void isPrimeNumber01() {
        boolean status = math.primeNumber(23);
        assertTrue(status);
        System.out.println("Test isPrimeNumber01");
    }

    @Test
    public void isPrimeNumber02() {
        boolean status = math.primeNumber(11);
        assertTrue(status);
        System.out.println("Test isPrimeNumber02");
    }

    @Test
    public void isPrimeNumber03() {
        boolean status = math.primeNumber(15);
        assertFalse(status);
        System.out.println("Test isPrimeNumber03");
    }

    @Test
    public void dice01() {
        int[] array =  math.dice(1);
        assertArrayEquals(new int[]{1, 2, 3, 4, 5, 6}, array);
        System.out.println("Test dice01");
    }

    @Test
    public void dice02() {
        int[] array =  math.dice(-6);
        assertArrayEquals(new int[]{-6, -5,-4,-3,-2,-1}, array);
        System.out.println("Test dice02");
    }

    @Test
    public void dice03() {
        int[] array =  math.dice(120);
        assertArrayEquals(new int[]{120,121,122,123,124,125}, array);
        System.out.println("Test dice03");
    }

    @Test
    public void signsSum01() {
        int result = math.signsSum('A','B');
        assertEquals(131,result);
        System.out.println("Test signsSum01");
    }

    @Test
    public void signsSum02() {
        int result = math.signsSum('D','D');
        assertEquals(136,result);
        System.out.println("Test signsSum01");
    }

    @Test
    public void signsComparison01() {
        boolean result = math.signsComparison('D','D');
        assertFalse(result);
        System.out.println("Test signsComparison01");
    }

    @Test
    public void signsComparison02() {
        boolean result = math.signsComparison('G','D');
        assertTrue(result);
        System.out.println("Test signsComparison02");
    }

    @Test
    public void stringComparison01() {
        boolean result = math.stringComparison("tak","o nie");
        assertFalse(result);
        System.out.println("Test stringComparison01");
    }

    @Test
    public void stringComparison02() {
        boolean result = math.stringComparison("very long sentence ","very short text");
        assertTrue(result);
        System.out.println("Test stringComparison02");
    }

    @Test
    public void stringLengthDifference01() {
        int result = math.stringLengthDifference("very long sentence ","very short text");
        assertEquals(4,result);
        System.out.println("Test stringComparisonLength01");
    }

    @Test
    public void stringLengthDifference02() {
        int result = math.stringLengthDifference("tak","nie");
        assertEquals(0,result);
        System.out.println("Test stringComparisonLength02");
    }
}