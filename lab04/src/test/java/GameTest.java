import org.junit.Test;

import static org.junit.Assert.*;
import static org.mockito.BDDMockito.given;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

public class GameTest {

    @Test
    public void symbol() {
        Game game = mock(Game.class);
        when(game.symbol()).thenReturn('G');
        char symbol = game.symbol();
        assertEquals('G',symbol);
    }

    @Test
    public void weight() {
        Game game = mock(Game.class);
        given(game.weight()).willReturn(4.8f);
        float weight = game.weight();
        assertEquals(4.8f,weight,2);
    }

    @Test
    public void power() {
        Game game = mock(Game.class);
        given(game.power()).willReturn(21.37);
        double power = game.power();
        assertEquals(21.37,power,1);
    }
}