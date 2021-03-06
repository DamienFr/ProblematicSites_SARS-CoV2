[![Build Status](https://travis-ci.com/W-L/ProblematicSites_SARS-CoV2.svg?branch=master)](https://travis-ci.com/W-L/ProblematicSites_SARS-CoV2)

- [Human-friendly version of the vcf file](#human-friendly-version-of-the-vcf-file)
- [Description of the columns in the vcf-version](#description-of-the-columns-in-the-vcf-version)


# Human-friendly version of the vcf file

|    POS    |REF|    ALT    |FILTER |                                  EXC                                  |   GENE    |AA_POS|AA_REF|  AA_ALT   |
|-----------|---|-----------|-------|-----------------------------------------------------------------------|-----------|------|------|-----------|
|1-55       |.  |.          |mask   |seq_end                                                                |.          |.     |.     |.          |
|76         |T  |W,A,C      |caution|ambiguous<br>neighbour_linked<br>narrow_src                            |.          |.     |.     |.          |
|78         |T  |Y,K,W,A,G  |caution|ambiguous<br>neighbour_linked<br>narrow_src                            |.          |.     |.     |.          |
|150        |T  |C,Y        |mask   |homoplasic<br>single_src<br>neighbour_linked                           |.          |.     |.     |.          |
|153        |T  |G,Y        |mask   |homoplasic<br>single_src<br>neighbour_linked                           |.          |.     |.     |.          |
|538        |A  |W          |caution|ambiguous                                                              |gene-orf1ab|91    |E     |X          |
|635        |C  |Y,T        |mask   |highly_ambiguous<br>homoplasic<br>narrow_src                           |gene-orf1ab|124   |R     |X,C        |
|660        |G  |K,A        |caution|ambiguous                                                              |gene-orf1ab|132   |G     |X,D        |
|759        |A  |D,T        |caution|ambiguous<br>single_src                                                |gene-orf1ab|165   |H     |X,L        |
|1001       |G  |A          |caution|ambiguous<br>amended                                                   |gene-orf1ab|246   |E     |K          |
|1707       |C  |Y,T,A      |mask   |highly_ambiguous<br>homoplasic<br>narrow_src                           |gene-orf1ab|481   |S     |X,F,Y      |
|1814       |A  |.          |caution|ambiguous<br>amended                                                   |gene-orf1ab|517   |K     |.          |
|1895       |G  |T,K        |mask   |ambiguous                                                              |gene-orf1ab|544   |V     |L,X        |
|1947       |T  |C,Y        |caution|ambiguous<br>narrow_src                                                |gene-orf1ab|561   |V     |A,X        |
|2087       |T  |Y          |caution|ambiguous                                                              |gene-orf1ab|608   |L     |L          |
|2091       |C  |T,Y        |mask   |highly_ambiguous<br>homoplasic<br>narrow_src                           |gene-orf1ab|609   |T     |I,X        |
|2094       |C  |T,Y        |mask   |highly_ambiguous<br>narrow_src                                         |gene-orf1ab|610   |S     |L,X        |
|2198       |G  |R,T,A      |mask   |homoplasic<br>ambiguous<br>narrow_src                                  |gene-orf1ab|645   |G     |X,C,S      |
|2604       |G  |T,K        |mask   |homoplasic<br>ambiguous<br>single_src                                  |gene-orf1ab|780   |G     |V,X        |
|3145       |G  |T          |mask   |homoplasic<br>single_src                                               |gene-orf1ab|960   |L     |F          |
|3564       |G  |T,K        |mask   |highly_ambiguous<br>highly_homoplasic<br>single_src                    |gene-orf1ab|1100  |G     |V,X        |
|3639       |G  |R,A        |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|1125  |G     |X,D        |
|3778       |A  |G          |mask   |homoplasic<br>single_src                                               |gene-orf1ab|1171  |T     |T          |
|4050       |A  |C          |mask   |homoplasic<br>single_src<br>amended                                    |gene-orf1ab|1262  |N     |T          |
|4463       |T  |C,Y        |caution|ambiguous<br>single_src<br>homoplasic                                  |gene-orf1ab|1400  |S     |P,X        |
|5011       |A  |M,C        |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|1582  |Q     |X,H        |
|5257       |A  |W,G,M      |mask   |highly_ambiguous<br>single_src                                         |gene-orf1ab|1664  |L     |X,L,X      |
|5393       |T  |Y          |caution|ambiguous<br>amended                                                   |gene-orf1ab|1710  |F     |X          |
|5498       |A  |.          |caution|ambiguous<br>amended                                                   |gene-orf1ab|1745  |K     |.          |
|5657       |G  |S,K,T,A    |caution|ambiguous<br>single_src                                                |gene-orf1ab|1798  |V     |X,X,L,I    |
|5736       |C  |T,Y        |mask   |homoplasic<br>single_src                                               |gene-orf1ab|1824  |A     |V,X        |
|5743       |G  |S,T        |mask   |highly_ambiguous<br>neighbour_linked<br>narrow_src                     |gene-orf1ab|1826  |E     |X,D        |
|5744       |T  |Y          |mask   |highly_ambiguous<br>neighbour_linked<br>narrow_src                     |gene-orf1ab|1827  |Y     |X          |
|5765       |G  |K,R        |caution|ambiguous<br>single_src<br>neighbour_linked                            |gene-orf1ab|1834  |G     |X,X        |
|5766       |G  |S          |caution|ambiguous<br>single_src<br>neighbour_linked                            |gene-orf1ab|1834  |G     |X          |
|6167       |G  |R,K        |mask   |ambiguous<br>single_src                                                |gene-orf1ab|1968  |V     |X,X        |
|6255       |C  |T          |mask   |highly_homoplasic<br>narrow_src                                        |gene-orf1ab|1997  |A     |V          |
|6309       |G  |T,R,A      |caution|neighbour_linked                                                       |gene-orf1ab|2015  |S     |I,X,N      |
|6310       |C  |A,T,M      |caution|neighbour_linked                                                       |gene-orf1ab|2015  |S     |R,S,X      |
|6312       |C  |A,M,T,G    |caution|neighbour_linked                                                       |gene-orf1ab|2016  |T     |K,X,I,R    |
|6866       |A  |W,T        |caution|ambiguous                                                              |gene-orf1ab|2201  |N     |X,Y        |
|6869       |A  |W,T        |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|2202  |T     |X,S        |
|6877       |G  |K,T        |caution|ambiguous<br>single_src                                                |gene-orf1ab|2204  |K     |X,N        |
|6971       |T  |C,W        |caution|neighbour_linked<br>single_src                                         |gene-orf1ab|2236  |L     |L,J        |
|6975       |G  |T          |caution|neighbour_linked<br>single_src                                         |gene-orf1ab|2237  |S     |I          |
|6977       |G  |A          |caution|neighbour_linked<br>single_src                                         |gene-orf1ab|2238  |V     |I          |
|7090       |T  |K          |caution|ambiguous<br>single_src                                                |gene-orf1ab|2275  |N     |X          |
|7305       |T  |K          |caution|ambiguous<br>single_src                                                |gene-orf1ab|2347  |M     |X          |
|7396       |T  |W,Y        |caution|ambiguous                                                              |gene-orf1ab|2377  |I     |I,I        |
|8022       |T  |K,G,C      |mask   |highly_ambiguous<br>highly_homoplasic<br>narrow_src                    |gene-orf1ab|2586  |V     |X,G,A      |
|8026       |A  |W,G,T      |mask   |ambiguous<br>homoplasic<br>narrow_src                                  |gene-orf1ab|2587  |A     |A,A,A      |
|8790       |G  |T,K        |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-orf1ab|2842  |G     |V,X        |
|8827       |T  |W          |mask   |ambiguous<br>neighbour_linked                                          |gene-orf1ab|2854  |I     |I          |
|8828       |G  |K,A        |mask   |ambiguous<br>neighbour_linked                                          |gene-orf1ab|2855  |A     |X,T        |
|9039       |C  |Y,M,T      |mask   |ambiguous<br>single_src                                                |gene-orf1ab|2925  |A     |X,X,V      |
|9471       |G  |S,C        |caution|ambiguous<br>single_src                                                |gene-orf1ab|3069  |R     |X,T        |
|10129      |T  |Y,C,W      |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-orf1ab|3288  |T     |T,T,T      |
|10239      |C  |M,A        |mask   |homoplasic<br>single_src                                               |gene-orf1ab|3325  |S     |X,Y        |
|11074      |C  |T,Y        |mask   |highly_homoplasic                                                      |gene-orf1ab|3603  |F     |F,F        |
|11083      |G  |T,K,A      |mask   |highly_homoplasic                                                      |gene-orf1ab|3606  |L     |F,X,L      |
|11535      |G  |T,K        |mask   |ambiguous<br>highly_homoplasic<br>single_src                           |gene-orf1ab|3757  |G     |V,X        |
|12506      |A  |R          |caution|ambiguous<br>single_src                                                |gene-orf1ab|4081  |K     |X          |
|13402      |T  |G,K,C      |mask   |homoplasic<br>narrow_src<br>amended                                    |gene-orf1ab|4379  |Y     |*,X,Y      |
|13408      |T  |K          |mask   |homoplasic<br>narrow_src<br>amended                                    |gene-orf1ab|4381  |C     |X          |
|13476      |C  |T,Y        |mask   |highly_ambiguous<br>narrow_src                                         |gene-orf1ab|4404  |C     |V,X        |
|13512      |A  |T,G        |caution|neighbour_linked                                                       |gene-orf1ab|4416  |T     |L,R        |
|13513      |G  |T,K        |caution|neighbour_linked                                                       |gene-orf1ab|4416  |T     |H,X        |
|13514      |G  |A,S        |caution|neighbour_linked                                                       |gene-orf1ab|4417  |G     |T,X        |
|13571      |G  |T,K        |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-orf1ab|4436  |G     |F,X        |
|13650      |T  |K          |caution|ambiguous<br>single_src                                                |gene-orf1ab|4462  |F     |X          |
|13686      |T  |A,Y        |caution|neighbour_linked                                                       |gene-orf1ab|4474  |H     |K,X        |
|13687      |G  |T          |caution|neighbour_linked                                                       |gene-orf1ab|4474  |H     |I          |
|13693      |A  |W,T        |caution|neighbour_linked                                                       |gene-orf1ab|4476  |E     |X,N        |
|14277      |G  |T,K        |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-orf1ab|4671  |R     |V,X        |
|15435      |A  |R,G        |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-orf1ab|5057  |E     |X,R        |
|15771      |T  |Y,W,K,D,H  |caution|ambiguous<br>single_src                                                |gene-orf1ab|5169  |A     |X,X,X,X,X  |
|15922      |T  |Y,C        |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|5219  |V     |C,C        |
|16210      |A  |W,D        |caution|ambiguous<br>single_src                                                |gene-orf1ab|5315  |A     |L,L        |
|16290      |T  |K          |mask   |highly_ambiguous<br>single_src                                         |gene-orf1ab|5342  |A     |X          |
|16537      |G  |K,T,R      |caution|ambiguous<br>single_src                                                |gene-orf1ab|5424  |S     |A,A,A      |
|16887      |C  |T,Y        |mask   |highly_homoplasic                                                      |gene-orf1ab|5541  |Y     |I,X        |
|18505      |G  |R          |caution|ambiguous<br>neighbour_linked                                          |gene-orf1ab|6080  |K     |K          |
|18506      |G  |K          |caution|ambiguous<br>neighbour_linked                                          |gene-orf1ab|6081  |G     |X          |
|18690      |T  |K,C        |caution|ambiguous<br>single_src                                                |gene-orf1ab|6142  |F     |X,S        |
|19298      |A  |D,W,T,R    |mask   |highly_ambiguous<br>single_src                                         |gene-orf1ab|6345  |Y     |X,X,L,X    |
|19299      |T  |Y,G        |mask   |homoplasic<br>ambiguous<br>narrow_src                                  |gene-orf1ab|6345  |Y     |X,R        |
|19338      |A  |R,G,M      |caution|highly_ambiguous<br>narrow_src                                         |gene-orf1ab|6358  |K     |X,R,X      |
|19339      |A  |M,W,R      |caution|ambiguous<br>single_src                                                |gene-orf1ab|6358  |K     |X,X,K      |
|19344      |T  |Y,K,C      |caution|ambiguous<br>amended                                                   |gene-orf1ab|6360  |A     |X,X,P      |
|19369      |T  |Y          |caution|ambiguous<br>amended                                                   |gene-orf1ab|6368  |P     |H          |
|19406      |G  |R,K,A      |caution|highly_ambiguous<br>single_src                                         |gene-orf1ab|6381  |G     |X,X,K      |
|19482      |T  |K,W        |caution|ambiguous<br>single_src                                                |gene-orf1ab|6406  |G     |X,X        |
|19484      |C  |T,Y        |mask   |highly_ambiguous<br>amended                                            |gene-orf1ab|6407  |A     |L,L        |
|19548      |A  |R,W,G,T,D  |mask   |ambiguous<br>single_src                                                |gene-orf1ab|6428  |S     |X,X,R,L,X  |
|19732      |G  |K,T,R      |caution|homoplasic<br>narrow_src                                               |gene-orf1ab|6489  |G     |V,V,V      |
|20056      |G  |K,A        |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|6597  |E     |X,K        |
|20123      |T  |Y,C        |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|6620  |I     |L,L        |
|20126      |G  |K,A,S,R    |caution|ambiguous<br>single_src<br>homoplasic                                  |gene-orf1ab|6621  |G     |X,K,Z,X    |
|20465      |A  |G,R,W      |mask   |highly_homoplasic<br>single_src                                        |gene-orf1ab|6734  |D     |V,X,X      |
|21302      |C  |T,A,S      |caution|neighbour_linked                                                       |gene-orf1ab|7013  |P     |Y,N,X      |
|21304      |C  |A,T,Y      |caution|neighbour_linked                                                       |gene-orf1ab|7013  |P     |Q,H,H      |
|21305      |G  |A,R        |caution|neighbour_linked                                                       |gene-orf1ab|7014  |R     |T,X        |
|21379      |T  |Y          |caution|ambiguous<br>single_src                                                |gene-orf1ab|7038  |S     |L          |
|21550      |A  |M,C        |mask   |ambiguous<br>homoplasic<br>narrow_src                                  |gene-orf1ab|7095  |N     |T,T        |
|21551      |A  |W,T,R      |mask   |ambiguous<br>homoplasic<br>narrow_src                                  |gene-orf1ab|7096  |N     |X,S,X      |
|21575      |C  |T,Y        |mask   |highly_homoplasic                                                      |gene-S     |5     |L     |F,X        |
|21609      |T  |K,W        |caution|ambiguous<br>single_src                                                |gene-S     |16    |V     |X,X        |
|21658      |C  |M,Y,H,T,G  |caution|ambiguous                                                              |gene-S     |32    |F     |X,F,X,F,L  |
|22329      |C  |Y,T        |caution|ambiguous<br>single_src                                                |gene-S     |256   |S     |X,L        |
|22335      |G  |T,K,A      |mask   |highly_ambiguous<br>amended                                            |gene-S     |258   |W     |L,X,*      |
|22389      |T  |Y,C        |caution|ambiguous<br>single_src                                                |gene-S     |276   |L     |X,P        |
|22393      |A  |G          |caution|ambiguous<br>amended                                                   |gene-S     |277   |L     |L          |
|22416      |T  |Y,C        |caution|ambiguous<br>neighbour_linked<br>single_src                            |gene-S     |285   |I     |X,T        |
|22420      |A  |W,T        |caution|ambiguous<br>neighbour_linked<br>single_src                            |gene-S     |286   |T     |T,T        |
|22488      |A  |R,M,C      |caution|ambiguous<br>amended                                                   |gene-S     |309   |E     |X,X,A      |
|22500      |A  |W,M        |caution|ambiguous<br>single_src                                                |gene-S     |313   |Y     |X,X        |
|22515      |T  |K,Y        |caution|ambiguous<br>narrow_src                                                |gene-S     |318   |F     |X,X        |
|22516      |T  |W,D,K,C,Y  |mask   |highly_ambiguous<br>single_src                                         |gene-S     |318   |F     |X,X,X,F,F  |
|22521      |T  |K,Y        |mask   |highly_ambiguous                                                       |gene-S     |320   |V     |X,X        |
|22661      |G  |T,S,A      |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-S     |367   |V     |F,X,I      |
|22802      |C  |M,A,T,Y    |mask   |homoplasic<br>single_src<br>amended<br>interspecific_contamination     |gene-S     |414   |Q     |X,K,*,X    |
|23116      |A  |W,T        |caution|ambiguous<br>single_src                                                |gene-S     |518   |L     |L,L        |
|23144      |A  |.          |caution|ambiguous<br>amended                                                   |gene-S     |528   |K     |.          |
|24389      |A  |W,M,C      |mask   |highly_homoplasic<br>highly_ambiguous<br>narrow_src<br>nanopore_adapter|gene-S     |943   |S     |X,X,R      |
|24390      |G  |T,S,K,C    |mask   |highly_homoplasic<br>highly_ambiguous<br>narrow_src<br>nanopore_adapter|gene-S     |943   |S     |I,X,X,T    |
|24622      |T  |Y          |mask   |highly_ambiguous<br>single_src                                         |gene-S     |1020  |A     |A          |
|24673      |A  |.          |caution|ambiguous<br>amended                                                   |gene-S     |1037  |S     |.          |
|24933      |G  |K,T        |mask   |highly_ambiguous<br>highly_homoplasic<br>narrow_src                    |gene-S     |1124  |G     |X,V        |
|24942      |A  |W,G,R      |caution|ambiguous<br>single_src                                                |gene-S     |1127  |D     |X,G,X      |
|25202      |T  |K          |mask   |highly_ambiguous                                                       |gene-S     |1214  |W     |X          |
|25381      |A  |C,R,M      |mask   |homoplasic<br>single_src                                               |gene-S     |1273  |T     |T,T,T      |
|25798      |A  |G          |caution|ambiguous<br>amended                                                   |gene-ORF3a |136   |K     |E          |
|26549      |C  |T,Y        |mask   |homoplasic<br>single_src                                               |gene-M     |9     |T     |T,T        |
|26700      |G  |T,K        |caution|ambiguous<br>single_src<br>homoplasic                                  |gene-M     |60    |V     |L,X        |
|26709      |G  |A,T,R      |caution|ambiguous<br>amended                                                   |gene-M     |63    |A     |T,S,X      |
|27534      |T  |W,C,Y      |caution|ambiguous<br>single_src                                                |gene-ORF7a |47    |H     |X,H,H      |
|27720      |T  |K          |caution|ambiguous<br>single_src                                                |gene-ORF7a |109   |F     |X          |
|27760      |T  |K,Y,A      |mask   |homoplasic<br>neighbour_linked                                         |.          |.     |.     |.          |
|27761      |T  |C          |mask   |homoplasic<br>neighbour_linked                                         |.          |.     |.     |.          |
|27784      |A  |W,G,T      |mask   |ambiguous<br>single_src                                                |.          |.     |.     |.          |
|27792      |T  |W          |caution|ambiguous<br>amended                                                   |.          |.     |.     |.          |
|28004      |T  |C,Y        |caution|neighbour_linked<br>single_src                                         |gene-ORF8  |37    |C     |C,C        |
|28005      |C  |T,G        |caution|neighbour_linked<br>single_src                                         |gene-ORF8  |38    |P     |S,A        |
|28006      |C  |T          |caution|neighbour_linked<br>single_src                                         |gene-ORF8  |38    |P     |L          |
|28008      |A  |G          |caution|neighbour_linked<br>single_src                                         |gene-ORF8  |39    |I     |V          |
|28253      |C  |Y,T,G,A,S  |mask   |highly_homoplasic                                                      |gene-ORF8  |120   |F     |F,F,L,L,X  |
|28517      |G  |S,K,T      |caution|ambiguous<br>single_src                                                |gene-N     |82    |D     |X,X,Y      |
|28676      |A  |M,C        |caution|ambiguous<br>single_src                                                |gene-N     |135   |T     |X,P        |
|28780      |A  |D,W,R      |caution|ambiguous<br>single_src                                                |gene-N     |169   |K     |X,X,K      |
|28881      |G  |A,R,T,K    |caution|neighbour_linked                                                       |gene-N     |203   |R     |K,X,M,X    |
|28882      |G  |A,R,T,K,S  |caution|neighbour_linked                                                       |gene-N     |203   |R     |R,R,S,X,X  |
|28883      |G  |C,S,A      |caution|neighbour_linked                                                       |gene-N     |204   |G     |R,X,R      |
|28985      |G  |R,D,T,K,A  |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-N     |238   |G     |X,X,C,X,S  |
|29037      |C  |T,Y,M      |mask   |homoplasic<br>ambiguous<br>single_src                                  |gene-N     |255   |S     |F,X,X      |
|29039      |A  |T,W        |mask   |homoplasic<br>ambiguous<br>single_src                                  |gene-N     |256   |K     |*,X        |
|29378      |A  |W          |caution|ambiguous<br>amended                                                   |gene-N     |369   |K     |X          |
|29425      |G  |T,S,A      |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-N     |384   |Q     |H,X,Q      |
|29427      |G  |S,K,A,T,R,C|caution|ambiguous<br>neighbour_linked<br>single_src                            |gene-N     |385   |R     |X,X,K,I,X,T|
|29428      |A  |R          |caution|ambiguous<br>neighbour_linked<br>single_src                            |gene-N     |385   |R     |R          |
|29553      |G  |A,T        |mask   |highly_homoplasic<br>single_src                                        |.          |.     |.     |.          |
|29737      |G  |K,A,T,S,C  |caution|ambiguous<br>single_src                                                |.          |.     |.     |.          |
|29786      |G  |K,C        |caution|homoplasic<br>single_src                                               |.          |.     |.     |.          |
|29827      |A  |G,T        |mask   |seq_end<br>highly_homoplasic<br>single_src                             |.          |.     |.     |.          |
|29830      |G  |T,A,C      |mask   |seq_end<br>highly_homoplasic<br>single_src                             |.          |.     |.     |.          |
|29804-29903|.  |.          |mask   |seq_end                                                                |.          |.     |.     |.          |


# Description of the columns in the vcf-version

The information presented in the table above is also [available as a .vcf formatted file](https://raw.githubusercontent.com/W-L/ProblematicSites_SARS-CoV2/master/problematic_sites_sarsCov2.vcf).

The VCF files have the 8 mandatory columns outlined in the VCF v4.3 specification, some of which contain non-standard content:

| Header         | Description                    |
|----------------|--------------------------------|
|CHROM           | Name of the reference sequence |
|POS             | 1-based position of the variation on the reference |
|ID              | NA |
|REF             | Reference base |
|ALT             | List of alternative alleles at the position (IUPAC ambiguity code) |
|QUAL            | NA |
|FILTER          | Masking recommendation (mask or interpret with caution) |
|INFO            | Key=value metadata pairs |

Metadata in the INFO column current includes the following:

| INFO keys      | Description                    |
|----------------|--------------------------------|
|SUB             | Initials of submitter          |
|EXC             | List of reasons for suggested exclusion (tags described in separate table) |
|SRC_COUNTRY     | Source country/countries of samples with the variant (excluded from the human-friendly VCF) |
|SRC_LAB         | Source laboratory/laboratories of samples with the variant, ordered to match the respective values in SRC_COUNTRY (excluded from the human-friendly VCF)  |
|GENE            | Position falls into range of this gene |
|AAPOS           | Position of amino acid residue within gene |
|REFAA           | Reference amino acid residue |
|ALTAA           | List of alternative amino acid residues (IUPAC ambiguity code) |


Descriptions of reasons for mask/caution (values for EXC in the INFO column) are as follows:

| Tag                         | Description                                                      |
|-----------------------------|------------------------------------------------------------------|
| seq_end                     | Alignment ends are affected by low coverage and high error rates |
| ambiguous                   | Sites which show an excess of ambiguous basecalls relative to the number of alternative alleles, often emerging from a single country or sequencing laboratory |
| amended                     | Previous sequencing errors which now appear to have been fixed in the latest versions of the GISAID sequences, at least in sequences from some of the sequencing laboratories |
| highly_ambiguous            | Sites with a very high proportion of ambiguous characters, relative to the number of alternative alleles |
| highly_homoplasic           | Positions which are extremely homoplasic - it is sometimes not necessarily clear if these are hypermutable sites or sequencing artefacts |
| homoplasic                  | Homoplasic sites, with many mutation events needed to explain a relatively small alternative allele count |
| interspecific_contamination | Cases (so far only one instance) in which the known sequencing issue is due to contamination from genetic material that does not have SARS-CoV-2 origin |
| nanopore_adapter            | Cases in which the known sequencing issue is due to the adapter sequences in nanopore reads |
| narrow_src                  | Variants which are found in sequences from only a few sequencing labs (usually two or three), possibly as a consequence of the same artefact reproduced independently |
| neighbour_linked            | Proximal variants displaying near perfect linkage |
| single_src                  | Only observed in samples from a single laboratory |

Suggestions, additions and issues are very gratefully received.
