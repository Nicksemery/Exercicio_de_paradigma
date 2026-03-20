package model;

import java.util.ArrayList;
import java.util.List;

public class Tarefas {


    private String nome;
    public List<String> lista = new ArrayList<>();


    public Tarefas() {}

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void adicionarNaLista(String nome) {
        this.lista.add(nome);
    }

    public void removerDaLista(String nome) {
        this.lista.remove(nome);
    }

    public void exibirLista() {
        for (String lista : this.lista) {
            System.out.println(lista);
        }
    }
}
