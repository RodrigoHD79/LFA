# Agente Virtual para Oficina Mecânica

Um agente virtual que identifica a necessidade do cliente, coleta informações sobre o veículo e direciona o atendimento para o serviço mecânico adequado.

## Funcionalidades principais

O agente é organizado em quatro especialidades:

### 1. Manutenção preventiva

- Troca de óleo e filtros
- Revisão periódica
- Verificação de freios
- Suspensão e alinhamento

### 2. Diagnóstico via scanner

- Leitura de códigos de erro
- Identificação de falhas eletrônicas
- Luz de injeção acesa
- Interpretação inicial dos códigos OBD2

### 3. Reparo mecânico

- Problemas no motor
- Falhas no sistema de transmissão
- Problemas na suspensão
- Falhas no sistema de arrefecimento

### 4. Orçamento e agendamento

- Estimativa inicial de custos
- Consulta de serviços necessários
- Solicitação de agendamento
- Encaminhamento para atendimento humano

---

## Base de conhecimento do agente de oficina

### Fatos coletados na triagem

`marca`, `modelo`, `ano`, `quilometragem`, `combustível`, `luzes_painel`, `sintoma_descrito`, `código_OBD2` (quando houver), `ruído`, `vazamento`, `cheiro`, `fumaça`, `tempo_do_problema`, `histórico_de_manutenção` e `data_da_última_troca_de_óleo`.

### Ordem de avaliação

A avaliação segue a ordem dos módulos. O **Módulo 0** é sempre avaliado primeiro e, se ele definir um estado de emergência, os módulos seguintes não são executados.

---

### Módulo 0: Emergência (prioridade máxima)

- **R0.1:** SE `fumaça_visível` OU `cheiro_de_combustível` OU `vazamento_de_combustível`, ENTÃO `estado = EMERGÊNCIA`, orientar a não ligar ou desligar o veículo, afastá-lo de fontes de ignição e encaminhar imediatamente para atendimento humano.
- **R0.2:** SE `luz_freio_vermelha` OU `pedal_de_freio_afundando` OU `freio_sem_resposta`, ENTÃO `estado = EMERGÊNCIA`, orientar a não dirigir e encaminhar para guincho ou atendimento humano imediato.
- **R0.3:** SE `luz_pressão_óleo` acesa, ENTÃO `estado = EMERGÊNCIA`, orientar a desligar o motor imediatamente, pois continuar rodando pode causar dano grave.
- **R0.4:** SE `luz_temperatura` acesa OU `indicador_temperatura` no vermelho OU `vapor_saindo_do_cofre`, ENTÃO `estado = EMERGÊNCIA`, orientar a parar com segurança, desligar o motor e aguardar esfriar antes de abrir o reservatório.
- **R0.5:** SE `luz_airbag` acesa OU `luz_ABS` acesa com perda de frenagem, ENTÃO `estado = ALTA_PRIORIDADE`, orientar a dirigir apenas o necessário e agendar atendimento no mesmo dia.
- **R0.6:** SE `direção_travada` OU `perda_súbita_de_direção`, ENTÃO `estado = EMERGÊNCIA`, orientar a parar com segurança e encaminhar para guincho.
- **R0.7:** SE `estado = EMERGÊNCIA`, ENTÃO interromper a triagem normal, não emitir estimativa de custo e encaminhar para humano.

### Módulo 1: Triagem

- **R1.1:** SE o cliente não informa modelo e ano, ENTÃO perguntar esses dados antes de qualquer outra etapa, pois códigos e recomendações dependem do veículo.
- **R1.2:** SE o veículo é diesel, elétrico ou híbrido, ENTÃO informar que o escopo do agente cobre apenas carros a gasolina ou flex e encaminhar para atendimento humano.
- **R1.3:** SE `ano_do_veículo < 1996`, ENTÃO informar que o diagnóstico OBD2 pode não estar disponível e encaminhar para avaliação presencial.
- **R1.4:** SE o cliente informa um código OBD2, ENTÃO validar o formato (uma letra P, B, C ou U seguida de quatro caracteres hexadecimais) antes de consultar a base.
- **R1.5:** SE o código é inválido, ENTÃO pedir que o cliente confira a leitura ou leve o veículo a um scanner.
- **R1.6:** SE o `sintoma_descrito` contém termos de mais de uma especialidade, ENTÃO fazer uma pergunta de desambiguação antes de rotear.

### Módulo 2: Roteamento

- **R2.1:** SE `luz_injeção` acesa OU `código_OBD2` presente, ENTÃO rotear para **Diagnóstico via Scanner**.
- **R2.2:** SE `sintoma_descrito` contém "troca de óleo", "revisão" ou "vencimento de manutenção", OU a quilometragem atingiu o intervalo de revisão, ENTÃO rotear para **Manutenção Preventiva**.
- **R2.3:** SE `sintoma_descrito` contém "freio fraco", "pedal mole", "ruído ao frear" ou "puxa para um lado", ENTÃO rotear para **Manutenção Preventiva** (verificação de freios) com FC 0.7, e para **Reparo Mecânico** se a verificação confirmar falha.
- **R2.4:** SE `sintoma_descrito` contém "barulho na suspensão", "batida ao passar em buraco" ou "carro inclinado", ENTÃO rotear para **Reparo Mecânico** (suspensão). SE `sintoma_descrito` contém "pneu desgastado irregularmente", ENTÃO rotear para **Manutenção Preventiva** (alinhamento).
- **R2.5:** SE `sintoma_descrito` contém "superaquecimento" sem luz acesa, "vazamento de líquido" ou "ventoinha sempre ligada", ENTÃO rotear para **Reparo Mecânico** (arrefecimento).
- **R2.6:** SE `sintoma_descrito` contém "trancos na troca de marcha", "patinando" ou "demora para engatar", ENTÃO rotear para **Reparo Mecânico** (transmissão).
- **R2.7:** SE nenhuma regra de roteamento disparou com FC acima de 0.5, ENTÃO fazer até três perguntas adicionais e, se persistir a dúvida, encaminhar para humano.

### Módulo 3: Diagnóstico via scanner

| Regra | Código | Hipótese | FC | Ação |
|---|---|---|---|---|
| R3.1 | P0300 | Falhas de ignição aleatórias ou múltiplas | 0.8 | Verificar velas, bobinas, cabos e sistema de combustível |
| R3.2 | P0301–P0304 | Falha de ignição no cilindro indicado pelo último dígito | 0.85 | Verificar vela e bobina desse cilindro; considerar troca de injetor se a falha persistir |
| R3.3 | P0171 | Mistura pobre (excesso de ar ou falta de combustível) | 0.7 | Verificar vazamentos na admissão, sensor MAF e pressão de combustível |
| R3.4 | P0172 | Mistura rica | 0.7 | Verificar sensor de oxigênio, injetores e filtro de ar |
| R3.5 | P0420 | Eficiência do catalisador abaixo do esperado | 0.6 | Verificar os sensores de oxigênio antes de trocar o catalisador, pois o sensor pode ser a causa |
| R3.6 | P0442 | Pequeno vazamento no sistema de evaporação (EVAP) | 0.6 | Verificar tampa do tanque e mangueiras |
| R3.7 | P0128 | Termostato possivelmente preso aberto ou sensor de temperatura defeituoso | 0.6 | Verificar nível de arrefecimento e funcionamento do termostato |
| R3.8 | P0562 | Tensão baixa no sistema elétrico | 0.6 | Testar bateria e alternador |
| R3.9 | P0700 | Falha no sistema de controle da transmissão | 0.6 | Ler os códigos específicos da transmissão com um scanner mais completo |

- **R3.10:** SE `código_OBD2` não consta na base, ENTÃO informar que o código foi lido mas não possui interpretação cadastrada, e encaminhar para humano com o código registrado.
- **R3.11:** SE `código_OBD2` presente E `luz_injeção` piscando, ENTÃO `estado = ALTA_PRIORIDADE`, orientar a reduzir a carga do motor e agendar atendimento no mesmo dia, pois a falha de ignição pode danificar o catalisador.
- **R3.12:** SE `código_OBD2` presente, ENTÃO informar que o código indica um circuito ou sistema com falha, não necessariamente a peça a ser trocada, e que a confirmação depende de inspeção presencial.

### Módulo 4: Manutenção preventiva

- **R4.1:** SE a quilometragem desde a última troca de óleo passou de 10.000 km OU 12 meses, ENTÃO recomendar troca de óleo e filtro, FC 0.9. O intervalo deve ser ajustado conforme o manual do fabricante, quando disponível.
- **R4.2:** SE a quilometragem atingiu múltiplo de 10.000 km OU 12 meses desde a última revisão, ENTÃO recomendar revisão periódica completa.
- **R4.3:** SE `quilometragem > 40.000 km` E não há registro de troca de fluido de freio, ENTÃO recomendar verificação de freios.
- **R4.4:** SE `sintoma_descrito` = "pneu desgastado de um lado", "volante vibra em alta velocidade" ou "puxa para um lado", ENTÃO recomendar alinhamento e balanceamento, FC 0.7.
- **R4.5:** SE `estado = EMERGÊNCIA` ou `ALTA_PRIORIDADE`, ENTÃO não aplicar recomendações preventivas e priorizar o encaminhamento.

### Módulo 5: Reparo mecânico

- **R5.1:** SE `sintoma_descrito` = "ruído metálico no motor" E `nível_de_óleo` baixo, ENTÃO hipótese = desgaste interno do motor, FC 0.5, ação = encaminhar para humano imediatamente.
- **R5.2:** SE `sintoma_descrito` = "barulho ao passar em lombadas" E ("carro inclinado" OU "amortecedor vazando"), ENTÃO hipótese = amortecedor ou coxim desgastado, FC 0.7, ação = inspeção da suspensão.
- **R5.3:** SE `sintoma_descrito` = "trepidação na direção" E "ao frear", ENTÃO hipótese = disco de freio empenado, FC 0.7, ação = inspeção de freios.
- **R5.4:** SE `sintoma_descrito` = "superaquecimento" E "vazamento de líquido" E "reservatório baixo", ENTÃO hipótese = vazamento no sistema de arrefecimento, FC 0.8, ação = teste de pressão e verificação de mangueiras e radiador.
- **R5.5:** SE `sintoma_descrito` = "trancos na troca de marcha" E transmissão automática, ENTÃO hipótese = desgaste de embreagens ou nível de fluido inadequado, FC 0.6, ação = verificar fluido e fazer diagnóstico da transmissão.
- **R5.6:** SE `sintoma_descrito` = "patinando" E transmissão manual E "embreagem demora a pegar", ENTÃO hipótese = desgaste da embreagem, FC 0.7.
- **R5.7:** SE `sintoma_descrito` = "falha de potência" E "acelerador responde mal" E `código_OBD2` não presente, ENTÃO rotear para **Diagnóstico via Scanner** com recomendação de leitura de códigos.

### Módulo 6: Orçamento

- **R6.1:** SE os serviços identificados são apenas de preventiva (troca de óleo, revisão, alinhamento), ENTÃO apresentar estimativa com faixa de valor da tabela de referência e informar que é preliminar.
- **R6.2:** SE os serviços incluem reparo com FC < 0.7 OU diagnóstico não confirmado, ENTÃO não gerar estimativa fechada e informar que o valor depende da inspeção presencial.
- **R6.3:** SE o serviço é troca de motor, transmissão ou sistema de freios completo, ENTÃO não gerar estimativa automática e encaminhar para orçamento humano.
- **R6.4:** SE o cliente pede preço exato antes da inspeção, ENTÃO informar que só é possível fornecer uma faixa estimada antes da avaliação presencial.

### Módulo 7: Agendamento e encaminhamento

- **R7.1:** SE `estado = EMERGÊNCIA`, ENTÃO encaminhar imediatamente para humano, sem agendamento automático.
- **R7.2:** SE `estado = ALTA_PRIORIDADE`, ENTÃO oferecer o primeiro horário disponível no mesmo dia.
- **R7.3:** SE `estado = NORMAL` E o cliente aceita o horário, ENTÃO registrar o agendamento com histórico completo: fatos coletados, hipóteses com FC, serviços sugeridos e observações.
- **R7.4:** SE o cliente não aceita nenhum horário OU pede atendimento humano, ENTÃO encaminhar para humano com o resumo da triagem.
- **R7.5:** SE o FC da hipótese principal < 0.5, ENTÃO encaminhar para humano em vez de agendar, para evitar agendamento baseado em suposição.

### Módulo 8: Acompanhamento e entrega

- **R8.1:** SE o serviço foi iniciado, ENTÃO atualizar o status para "em diagnóstico", "aguardando peça", "em execução" ou "concluído", conforme o mecânico registrar.
- **R8.2:** SE o status = "concluído", ENTÃO avisar o cliente que o veículo está pronto e registrar os serviços executados.
- **R8.3:** SE o serviço foi concluído E há intervalo de próxima manutenção definido, ENTÃO registrar a data ou quilometragem da próxima preventiva e lembrar o cliente no momento apropriado.

---

### Regra de combinação de certeza

Quando duas regras com FC positivo concluem a mesma hipótese, o FC combinado é calculado por:

```
FC = FC1 + FC2 × (1 − FC1)
```

**Exemplo:** se duas regras chegam à mesma hipótese com FC 0.7 e 0.5, o resultado é `0.7 + 0.5 × 0.3 = 0.85`.

> **Observação:** os valores de FC são ilustrativos e devem ser validados com um mecânico antes da entrega final.
