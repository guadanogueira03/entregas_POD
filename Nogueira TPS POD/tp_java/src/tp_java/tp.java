package tp_java;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

class PPTLS { 
    private String jugador1;
    private String jugador2;
    private static final Map<String, List<String>> reglas = new HashMap<>();

    static {
        reglas.put("Piedra", List.of("Tijera", "Lizard"));
        reglas.put("Papel", List.of("Piedra", "Spock"));
        reglas.put("Tijera", List.of("Papel", "Lizard"));
        reglas.put("Lizard", List.of("Papel", "Spock"));
        reglas.put("Spock", List.of("Piedra", "Tijera"));
    }

    public PPTLS(String jugador1, String jugador2) {
        this.jugador1 = jugador1;
        this.jugador2 = jugador2;
    }

    public String jugar() {
        if (jugador1.equals(jugador2)) {
            return "Empate";
        } else if (reglas.get(jugador1).contains(jugador2)) {
            return "Jugador 1 gana";
        } else {
            return "Jugador 2 gana";
        }
    }
}

// Cinco ejemplos de jugadas

public class tp {
    public static void main(String[] args) {
        PPTLS juego = new PPTLS("Piedra", "Tijera");
        System.out.println(juego.jugar()); 
        
        PPTLS juego2 = new PPTLS("Lizard", "Spock");
        System.out.println(juego2.jugar()); 
        
        PPTLS juego3 = new PPTLS("Papel", "Papel");
        System.out.println(juego3.jugar());
        
        PPTLS juego4 = new PPTLS("Piedra", "Spock");
        System.out.println(juego4.jugar()); 
        
        PPTLS juego5 = new PPTLS("Piedra", "Papel");
        System.out.println(juego5.jugar()); 
        
    }
}


