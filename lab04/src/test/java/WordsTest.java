import org.junit.Test;

import static org.junit.Assert.*;
import static org.mockito.BDDMockito.given;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;


public class WordsTest {

    @Test
    public void money() {
        Words words = mock(Words.class);
        when(words.money()).thenReturn(1111);
        int value = words.money();
        assertEquals(1111, value);
    }


    @Test
    public void house() {
        Words words = mock(Words.class);
        when(words.house()).thenReturn("Cannabis");
        String word = words.house();
        assertEquals("Cannabis", word);
    }

    @Test
    public void gameOn() {
        Words words = mock(Words.class);
        given(words.gameOn()).willReturn(true);
        boolean stan = words.gameOn();
        assertTrue(stan);
    }
}