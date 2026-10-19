# ej 0.0.2 training data (generated)

Pool `pool_i` (sha256 `510e356463f36870ef6ca8d48ec33a7378462e2945111fefb73edc4138a50c1e`), 17,629 records in 18 groups: the whole ej 0.0.1 pool (9,719 records; `docs/data-card.md`: Typed Decisions, in-house support tickets, Banking77, CLINC150, GoEmotions) plus 80 questions from each Bekko subset below (7,910 records). Bekko is `hotchpotch/bekko-system-one-dataset-v0` @ `9c673a09c31e145684ab9915871afa72ba40a383`, train splits only, questions chosen by ascending sha256 of the case id. The four Bekko subsets that repeat 0.0.1's own sources (banking77, clinc, go_emotions, laya__typed_decisions) are not added. Upstream licences are Bekko's 2026-09-30 audit (`license-audit.json`); several are "qualified" (the underlying text carries source-specific terms) and are used under a permissive scope. The weights stay CC BY-SA 4.0. No S1MB test case was used for training or selection; selection used ej's four development suites and the Bekko validation splits.

**Not a plain `ej.train fit` output.** The fit left 2,816 non-finite entries in the relational reader's weight vector (an L-BFGS fit, state tensor `t46`). That one vector was refitted on the same inputs with the same L2 (0.001) and swapped in; its vocabulary order is identical and the finite entries of the original agree with the refit to 0.003 (correlation 0.99996). Every other tensor is the fit's.

| family (group id) | Bekko subset | questions | upstream dataset | upstream licence |
|---|---|---:|---|---|
| intent | bitext | 80 | bitext/Bitext-customer-support-llm-chatbot-training-dataset | cdla-sharing-1.0 |
| intent | canttalk | 80 | nvidia/CantTalkAboutThis-Topic-Control-Dataset | CC BY 4.0 |
| intent | circa | 80 | google-research-datasets/circa | CC BY 4.0 |
| intent | esci | 80 | tasksource/esci | Apache-2.0 |
| intent | hwu64 | 80 | FastFit/hwu_64 | CC BY 4.0 |
| intent | massive | 80 | AmazonScience/massive | CC BY 4.0 |
| intent | minds14 | 80 | PolyAI/minds14 | CC BY 4.0 |
| intent | mtop | 80 | tasksource/mtop | CC BY-SA 4.0 |
| intent | nlupp | 88 | https://github.com/PolyAI-LDN/task-specific-datasets | CC BY 4.0 |
| intent | sgd | 80 | https://github.com/google-research-datasets/dstc8-schema-guided-dialogue | CC BY-SA 4.0 |
| intent | snips | 80 | https://github.com/sonos/nlu-benchmark | CC0-1.0 |
| intent | taskmaster | 80 | https://github.com/google-research-datasets/Taskmaster | CC BY 4.0 |
| jev-control | open_jev__drone-control-v1 | 80 | ZefanCai/Open-Jev | CC0-1.0 |
| jev-control | open_jev__painting-geometry-v1 | 80 | ZefanCai/Open-Jev | CC0-1.0 |
| jev-control | open_jev__snake-v1 | 80 | ZefanCai/Open-Jev | CC0-1.0 |
| jev-control | open_jev__tic_tac_toe-v1 | 80 | ZefanCai/Open-Jev | CC0-1.0 |
| jev-control | open_jev__tile_platformer-v1 | 80 | ZefanCai/Open-Jev | CC0-1.0 |
| jev-control | open_jev__trex_runner-v1 | 28 | ZefanCai/Open-Jev | CC0-1.0 |
| jev-control | open_jev__vizdoom-basic-v1 | 80 | ZefanCai/Open-Jev | CC0 (numeric data) |
| jev-extraction | open_jev__amount-extraction-control-v1 | 80 | ZefanCai/Open-Jev | CC0-1.0 |
| jev-extraction | open_jev__citation-control-v1 | 80 | ZefanCai/Open-Jev | CC0-1.0 |
| jev-extraction | open_jev__email-selection-control-v1 | 80 | ZefanCai/Open-Jev | CC0-1.0 |
| jev-extraction | open_jev__entity-alignment-control-v1 | 80 | ZefanCai/Open-Jev | CC0-1.0 |
| jev-extraction | open_jev__ir-control-v1 | 80 | ZefanCai/Open-Jev | CC0-1.0 |
| jev-extraction | open_jev__mailroom-control-v1 | 80 | ZefanCai/Open-Jev | CC0-1.0 |
| jev-extraction | open_jev__phone-extraction-control-v1 | 80 | ZefanCai/Open-Jev | CC0-1.0 |
| jev-extraction | open_jev__sponsor-segment-control-v1 | 80 | ZefanCai/Open-Jev | CC0-1.0 |
| jev-workflow | open_jev__browser-control-v1 | 80 | ZefanCai/Open-Jev | CC0-1.0 |
| jev-workflow | open_jev__context-retention-control-v1 | 80 | ZefanCai/Open-Jev | CC0-1.0 |
| jev-workflow | open_jev__reasoning-control-v1 | 80 | ZefanCai/Open-Jev | CC0-1.0 |
| jev-workflow | open_jev__silent-failure-control-v1 | 80 | ZefanCai/Open-Jev | CC0-1.0 |
| jev-workflow | open_jev__workflow-controls-v1__agent_trace_observability | 80 | ZefanCai/Open-Jev | CC0-1.0 |
| jev-workflow | open_jev__workflow-controls-v1__customer_service | 80 | ZefanCai/Open-Jev | CC0-1.0 |
| jev-workflow | open_jev__workflow-controls-v1__invoice_processing | 80 | ZefanCai/Open-Jev | CC0-1.0 |
| jev-workflow | open_jev__workflow-controls-v1__security_incidents | 80 | ZefanCai/Open-Jev | CC0-1.0 |
| nli | babi_nli | 80 | tasksource/babi_nli | BSD |
| nli | contract_nli | 85 | https://github.com/stanfordnlp/contract-nli | CC BY 4.0 |
| nli | corr2cause | 80 | tasksource/corr2cause | MIT |
| nli | defeasible_nli | 80 | tasksource/defeasible-nli | Apache-2.0 / CC BY-SA 4.0 |
| nli | fol_nli | 80 | tasksource/FOL-nli | Apache-2.0 |
| nli | hans | 80 | tasksource/hans | MIT |
| nli | lexcomp | 80 | tasksource/lexcomp-nc-relation | Apache-2.0 |
| nli | logical_entailment | 80 | tasksource/logical-entailment | Apache-2.0 |
| nli | mnli | 80 | nyu-mll/multi_nli | CC BY 3.0 / CC BY-SA 3.0 / OANC / public domain |
| nli | monotonicity | 80 | tasksource/monotonicity-entailment | Apache-2.0 |
| nli | natural_logic | 80 | tasksource/naturallogic | Apache-2.0 |
| nli | nlsat | 80 | tasksource/nlsat | Apache-2.0 |
| nli | paws | 80 | google-research-datasets/paws | Google custom license; Wikipedia text: CC BY-SA / GFDL |
| nli | plane | 80 | tasksource/PLANE-ood | CC BY 2.0 |
| nli | ruletaker | 80 | tasksource/ruletaker | Apache-2.0 |
| nli | scitail | 80 | allenai/scitail | Apache-2.0 |
| nli | scone | 80 | tasksource/scone | CC0-1.0 |
| nli | sdoh_nli | 80 | tasksource/SDOH-NLI | CC BY 4.0 |
| nli | snli | 80 | stanfordnlp/snli | CC BY-SA 4.0 |
| nli | space_nli | 80 | tasksource/SpaceNLI | MIT |
| nli | temporal_nli | 80 | tasksource/temporal-nli | Apache-2.0 |
| nli | tracie | 80 | tasksource/tracie | Apache-2.0 |
| qa-mc | aqua_rat | 80 | deepmind/aqua_rat | Apache-2.0 |
| qa-mc | arc | 80 | allenai/ai2_arc | CC BY-SA 4.0 |
| qa-mc | boolq | 80 | google/boolq | CC BY-SA 3.0 |
| qa-mc | commonsense_qa | 80 | tau/commonsense_qa | MIT |
| qa-mc | commonsense_qa2 | 80 | tasksource/commonsense_qa_2.0 | CC BY 4.0 |
| qa-mc | copa | 80 | aps/super_glue | BSD-2-Clause (COPA) |
| qa-mc | cosmos_qa | 80 | Samsoup/cosmos_qa | CC BY 4.0 |
| qa-mc | fig_qa | 80 | nightingal3/fig-qa | MIT |
| qa-mc | gsm8k | 80 | openai/gsm8k | MIT |
| qa-mc | openbookqa | 80 | allenai/openbookqa | Apache-2.0 |
| qa-mc | piqa | 80 | lighteval/piqa | AFL-3.0 |
| qa-mc | qasc | 80 | allenai/qasc | CC BY 4.0 |
| qa-mc | qasper | 80 | allenai/qasper | CC BY 4.0 |
| qa-mc | quartz | 80 | allenai/quartz | CC BY 4.0 |
| qa-mc | ropes | 80 | allenai/ropes | CC BY 4.0 |
| qa-mc | social_iqa | 80 | baber/social_i_qa | CC BY 4.0 |
| qa-mc | squad2 | 80 | rajpurkar/squad_v2 | CC BY-SA 4.0 |
| qa-mc | winogrande | 80 | allenai/winogrande | Apache-2.0 |
| qa-mc | wiqa | 80 | allenai/wiqa | Apache-2.0 |
| quality-sentiment | argument_quality | 80 | ibm-research/argument_quality_ranking_30k | CC BY 3.0 (conflicting source notices) |
| quality-sentiment | helpsteer | 80 | nvidia/HelpSteer | CC BY 4.0 |
| quality-sentiment | helpsteer2 | 80 | nvidia/HelpSteer2 | CC BY 4.0 |
| quality-sentiment | helpsteer3 | 81 | nvidia/HelpSteer3 | CC BY 4.0 |
| quality-sentiment | oasst1 | 80 | OpenAssistant/oasst1 | Apache-2.0 |
| quality-sentiment | poem_sentiment | 80 | google-research-datasets/poem_sentiment | CC BY 4.0 |
| relevance | synthetic_relevance__all_nli | 80 | sentence-transformers/all-nli | SNLI: CC BY-SA 4.0; MultiNLI: CC BY 3.0 / CC BY-SA 3.0 / OANC / public domain |
| relevance | synthetic_relevance__arxiv | 80 | hotchpotch/arxiv-ir-simulated-search-queries; open-index/open-arxiv | CC0 (metadata); paper licenses vary |
| relevance | synthetic_relevance__bge_m3__hotpotqa | 80 | Shitao/bge-m3-data: hotpotqa; hotpotqa/hotpot_qa | CC BY-SA 4.0; No aggregate license declared; constituent terms apply |
| relevance | synthetic_relevance__bge_m3__miracl_en | 80 | Shitao/bge-m3-data: miracl_en; miracl/miracl | Apache-2.0; Wikipedia text: CC BY-SA / GFDL; No aggregate license declared; constituent terms apply |
| relevance | synthetic_relevance__bge_m3__mr-tydi_english | 80 | Shitao/bge-m3-data: mr-tydi_english; castorini/mr-tydi | Apache-2.0; Wikipedia text: CC BY-SA / GFDL; No aggregate license declared; constituent terms apply |
| relevance | synthetic_relevance__bge_m3__nq | 80 | Shitao/bge-m3-data: nq; google-research-datasets/natural_questions | CC BY-SA 3.0; No aggregate license declared; constituent terms apply |
| relevance | synthetic_relevance__bge_m3__pubmed_qa_labeled | 80 | Shitao/bge-m3-data: pubmed_qa_labeled; qiaojin/PubMedQA | MIT (dataset); abstract rights vary; No aggregate license declared; constituent terms apply |
| relevance | synthetic_relevance__bge_m3__squad | 80 | Shitao/bge-m3-data: squad; rajpurkar/squad | CC BY-SA 4.0; No aggregate license declared; constituent terms apply |
| relevance | synthetic_relevance__bge_m3__trivia | 80 | Shitao/bge-m3-data: trivia; mandarjoshi/trivia_qa | Apache-2.0; No aggregate license declared; constituent terms apply |
| relevance | synthetic_relevance__coco_captions | 80 | sentence-transformers/coco-captions | CC BY 4.0 (captions) |
| relevance | synthetic_relevance__codesearch | 80 | nomic-ai/nomic-embed-unsupervised-data | MIT (tools); source-code licenses vary |
| relevance | synthetic_relevance__fineweb | 80 | HuggingFaceFW/fineweb-edu; hotchpotch/fineweb-ir-simulated-search-queries | ODC-By 1.0 (database); source-page rights vary |
| relevance | synthetic_relevance__natural_questions | 80 | google-research-datasets/natural_questions; sentence-transformers/natural-questions | CC BY-SA 3.0 |
| relevance | synthetic_relevance__pubmed | 80 | hotchpotch/pubmed-abstract-ir-simulated-search-queries; slinusc/PubMedAbstractsSubset | CC0 (metadata); abstract rights vary |
| relevance | synthetic_relevance__trivia_qa | 80 | mandarjoshi/trivia_qa; sentence-transformers/trivia-qa | Apache-2.0 |
| relevance | synthetic_relevance__wikipedia_hard_negatives_english | 80 | hotchpotch/wikipedia-english-ir-simulated-search-queries | CC BY-SA 4.0 / GFDL |
| safety | aegis2 | 81 | nvidia/Aegis-AI-Content-Safety-Dataset-2.0 | CC BY 4.0 |
| safety | civil_comments | 84 | google/civil_comments | CC0-1.0 |
| safety | ethics | 80 | hendrycks/ethics | MIT |
| safety | gretel_pii | 73 | gretelai/gretel-pii-masking-en-v1 | Apache-2.0 |
| safety | hh_rlhf | 80 | Anthropic/hh-rlhf | MIT |
| safety | measuring_hate | 80 | ucberkeley-dlab/measuring-hate-speech | CC BY 4.0 |
| safety | sms_spam | 80 | ucirvine/sms_spam | CC BY 4.0 |
| syntax-logic | arct | 80 | tasksource/arct | Apache-2.0 |
| syntax-logic | blimp | 80 | nyu-mll/blimp | CC BY 4.0 |
| syntax-logic | boardgameqa | 80 | tasksource/Boardgame-QA | CC BY 4.0 |
| syntax-logic | creak | 80 | amydeng2000/CREAK | MIT (repository); data license unconfirmed |
| syntax-logic | feasibility_qa | 80 | tasksource/feasibilityQA | MIT |
| syntax-logic | spartqa | 80 | tasksource/spartqa-mchoice | MIT |
| syntax-logic | stepgame | 80 | tasksource/stepgame | MIT |
| syntax-logic | strategyqa | 80 | tasksource/strategy-qa | MIT |
| topic-entity | dbpedia | 80 | fancyzhx/dbpedia_14 | CC BY-SA 3.0 |
| topic-entity | few_nerd | 79 | DFKI-SLT/few-nerd | CC BY-SA 4.0 |
| topic-entity | patent_similarity | 80 | tasksource/patent-phrase-similarity | CC BY 4.0 |
| topic-entity | ud_ewt | 79 | universal-dependencies/universal_dependencies | CC BY-SA 4.0 |

## Excluded subsets

| Bekko subset | reason |
|---|---|
| abductive_nli | allenai/art licence unknown after 2026-09-30 review |
| agnews | licence unknown |
| bge-hn-colliee | COLIEE access terms unresolved |
| bge-hn-msmarco | Microsoft Research terms, non-commercial research only |
| ethos | GPL-3.0 |
| followir | Robust04 / Washington Post corpora restricted |
| gooaq | dataset README: non-commercial research restriction |
| laya__ag_news | licence unknown |
| laya__enron_spam | no dataset licence located |
| laya__phishing | LGPL-3.0 |
| open_jev__customer-control-v1 | upstream question wording licence not verified |
| scicite | original dataset licence not located |
| synthetic_relevance__agnews | licence unknown |
| synthetic_relevance__bge_m3__msmarco | Microsoft Research terms, non-commercial research only |
| synthetic_relevance__gooaq | dataset README: non-commercial research restriction |

Also not used: 17 document-ranking subsets (no choice/noul/score decision).
