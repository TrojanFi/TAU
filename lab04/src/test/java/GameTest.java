import org.junit.Test;

import static org.junit.Assert.*;
import static org.mockito.ArgumentMatchers.floatThat;
import static org.mockito.BDDMockito.given;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

public class GameTest {

    @Test
    public void symbol() {
        Game game = mock(Game.class);
        when(game.symbol()).thenReturn('Z');
        char symbol = game.symbol();
        assertEquals('Z',symbol);
    }

    @Test
    public void weight() {
        Game game = mock(Game.class);
        given(game.weight()).willReturn(2.4f);
        float weight = game.weight();
        assertEquals(2.4f,weight,2);
    }

    @Test
    public void power() {
        Game game = mock(Game.class);
        given(game.power()).willReturn(45.5);
        double power = game.power();
        assertEquals(45.5,power,1);
    }
}