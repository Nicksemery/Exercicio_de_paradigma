import model.Tarefas;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {


        Tarefas tarefas = new Tarefas();
        Scanner sc = new Scanner(System.in);
        System.out.println("Bem vindo ao gerenciador de tarefas diarias!");

        while (true) {
            System.out.println("-------------------------------------------");
            System.out.println("Início");
            System.out.println("Digite [1] para adicionar uma tarefa à lista");
            System.out.println("Digite [2] para mostrar a lista de tarefas");
            System.out.println("Digite [3] para remover uma tarefa");
            System.out.println("Digite [0] para sair do programa");
            System.out.println("-------------------------------------------");
            switch (sc.nextInt()) {
                case 1 -> {
                    System.out.println("Adicionar tarefa: ");
                    tarefas.adicionarNaLista(sc.next());
                    System.out.println("Adicionado com sucesso!");
                }
                case 2 -> {
                    System.out.println("Tarefas até agora: ");
                    tarefas.exibirLista();
                }
                case 3 -> {
                    System.out.println("Remover tarefa: ");
                    tarefas.removerDaLista(sc.next());
                    System.out.println("Removido com sucesso!");
                }
                case 0 -> {
                    System.out.println("Saindo...");
                    return;
                }
                default -> System.out.println("Opço invalida!");
            }
        }
    }
}