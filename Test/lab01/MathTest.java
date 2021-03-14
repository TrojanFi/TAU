package lab01;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.w3c.dom.ls.LSOutput;

import java.lang.reflect.Array;
import java.util.Arrays;

import static org.junit.Assert.*;

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
    public void dice01() throws Exception{
        int[] array =  math.dice(1);
        assertArrayEquals(new int[]{1, 2, 3, 4, 5, 6}, array);
        System.out.println("Test dice01");
    }

    @Test
    public void dice02() throws Exception{
        int[] array =  math.dice(-6);
        assertArrayEquals(new int[]{-6, -5,-4,-3,-2,-1}, array);
        System.out.println("Test dice02");
    }
}