import org.junit.Test;

import static org.junit.Assert.*;
import static org.mockito.ArgumentMatchers.booleanThat;
import static org.mockito.BDDMockito.given;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;


public class WordsTest {

    private String word;

    @Test
    public void money() {
        Words words = mock(Words.class);
        when(words.money()).thenReturn(100);
        int value = words.money();
        assertEquals(100, value);
    }


    @Test
    public void house() {
        Words words = mock(Words.class);
        when(words.house()).thenReturn("house");
        word = words.house();
        assertEquals("house",word);
    }

    @Test
    public void gameOn() {
        Words words = mock(Words.class);
        given(words.gameOn()).willReturn(false);
        boolean stan = words.gameOn();
        assertFalse(stan);
    }
}