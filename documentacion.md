En el excel orginal se compone de 3 paginas , asi es llamado archivo auqne voy a analizarlo por anchivos diferentes:

# df_julio, pagina 1 del excel orginial, vienen los datos de julio (altas-bajas)
son 24 columnas y 48430 datos 

 0  Convenio Aplicable                                23800 non-null  str  
  
    3 categorias:                         
            NaN                    24631       50.857922 %
            Sí                     13270       27.399806 % 
            No                     10530       21.742273 % 

        ojo el 50% de los datos de esta categoria son nulos

 1  Localización País                                  48431 non-null  str  
        2 paises, ESpaña y Brasil
            Cantidad  Porcentaje (%)
            Localización País                          
            Brasil                32412       66.924078
            España                16019       33.075922
    
             
 2   Área Funcional                                     15995 non-null  str 
        tiene 74 areas funcionales

        Cantidad  Porcentaje (%)
        Área Funcional                                                              
            NaN                                                    32436       66.973633
            Red - Control de Operaciones de Red                     4200        8.672131
            Red - Ingeniería de Red de Acceso y Troncal             3995        8.248849
            B2B Empresas y Pymes - Ventas B2B                       1274        2.630547
            B2C Ventas - Gestión Canal Telefónico                    872        1.800500
            B2B Empresas y Pymes - Backoffice de Atención            560        1.156284
            B2C Atención al Cliente - Backoffice                     426        0.879602
            Red - Planificación Tecnológica                          386        0.797010
            B2C Atención al Cliente - At. Presencial / At. ...       382        0.788751
            TI - Aplicaciones/Desarrollo                             371        0.766038
            B2B Empresas y Pymes - Preventa Grandes Cuentas          368        0.759844
            B2C Marketing - Marketing de Producto                    291        0.600855
            Calidad y Procesos - Mejora procesos y control ...       244        0.503810
            Finanzas, Adm. y CDG - Créditos y Cobros                 190        0.392311
            TI - Producción                                          177        0.365468
            B2C Ventas - Gestión Canal Online                        163        0.336561
            Op. Comerciales - Facturación                            158        0.326237
            Finanzas, Adm. y CDG - Planificación Financiera          149        0.307654
            B2B Empresas y Pymes - Planificación Comercial           149        0.307654
            B2C Ventas - Gestión Canales Comerciales (Dir. ...       126        0.260164
            B2B Empresas y Pymes - Marketing                          99        0.204415
            Op. Comerciales - Soporte de Operaciones de Ventas        95        0.196155
            RRHH - Generalista RRHH / Business Partner                85        0.175507
            B2C Marketing - Planificación de Marketing                79        0.163119
            B2C Marketing - Marketing de Clientes                     64        0.132147
            RRHH - Relaciones Laborales y Sindicales                  59        0.121823
            Negocio Mayorista - Gestión de Clientes                   58        0.119758
            B2C Marketing - BI                                        58        0.119758
            B2C Marketing (sin clasificar)                            52        0.107369
            Negocio Mayorista - Ventas                                51        0.105304
            Op. Comerciales - Logística y Distribucion                51        0.105304
            Finanzas, Adm. y CDG - (sin clasificar)                   48        0.099110
            Servicios Generales - Prestación de servicios             40        0.082592
            B2B Empresas y Pymes - Preventa Generalista               40        0.082592
            Asesoría Jurídica - Especialidad                          40        0.082592
            Op. Comerciales - Adm. Comercial y Liq. Comisiones        38        0.078462
            Seguridad y Prot. - Seguridad Física                      36        0.074333
            TI - Estrategia y Gobierno                                36        0.074333
            Compras (sin clasificar)                                  34        0.070203
            B2C Marketing - Publicidad, Comunicación y Eventos        33        0.068138
            Asesoría Jurídica (sin clasificar)                        32        0.066073
            Asesoría Jurídica - Generalista/Multidisciplina           32        0.066073
            Seguridad y Prot. - Continuidad de operaciones            28        0.057814
            RRHH - Formación                                          28        0.057814
            B2B Empresas y Pymes (sin clasificar)                     27        0.055749
            RRHH - Talento y Desarrollo                               25        0.051620
            B2C Marketing - Terminales                                22        0.045425
            Estrategia - Planificación Estratégica                    19        0.039231
            B2C Ventas - Planificación Comercial                      16        0.033037
            Dentro de Convenio (sin clasificar)                       14        0.028907
            Seguridad y Prot. - Generalista/Multidisciplina           13        0.026842
            Estrategia - Proyectos Estratégicos                       13        0.026842
            Media - Generalista/Multidisciplina                       12        0.024778
            Negocio Mayorista - Generalista/Multidisciplina           12        0.024778
            Red - Inst. y Manten. Red de Acceso y Troncal             10        0.020648
            RRHH - Organización                                       10        0.020648
            Auditoría y Control Int. - Auditoría                      10        0.020648
            Auditoría y Control Int. - Intervención y Contr...        10        0.020648
            Servicios Generales - Inmobiliario e instalaciones        10        0.020648
            Direccion                                                  9        0.018583
            Finanzas, Adm. y CDG - Tesorería                           8        0.016518
            RRHH - Selección y Reclutamiento                           7        0.014454
            Finanzas, Adm. y CDG - Generalista/Multidisciplina         7        0.014454
            B2B Empresas y Pymes - Venta Especialista                  7        0.014454
            Calidad y Procesos (sin clasificar)                        7        0.014454
            RRHH - Planificación y Reporting                           6        0.012389
            RRHH - Compensación y Beneficios                           6        0.012389
            B2C Atención al Cliente - Gest. calidad y satis...         5        0.010324
            Finanzas, Adm. y CDG - Planificación y Control ...         4        0.008259
            Estrategia - Aceleración de Negocios                       3        0.006194
            RRHH (sin clasificar)                                      2        0.004130
            Estrategia - Generalista/Multidisciplina                   2        0.004130
            Soporte a la Dirección (Secretaria / Asistente)            1        0.002065
            Calidad y Procesos - Generalista/Multidisciplina           1        0.002065

    destaca 66% de nulos 

    En las que mas gente trabaja:
  
                    Red - Control de Operaciones de Red	4200	8.672131
                    Red - Ingeniería de Red de Acceso y Troncal	3995	8.248849
                    B2B Empresas y Pymes - Ventas B2B	1274	2.630547
                    B2C Ventas - Gestión Canal Telefónico	872	1.800500

    En la que menos gente trabaja:

                    Estrategia - Aceleración de Negocios	3	0.006194
                    RRHH (sin clasificar)	2	0.004130
                    Estrategia - Generalista/Multidisciplina	2	0.004130
                    Soporte a la Dirección (Secretaria / Asistente)	1	0.002065
                    Calidad y Procesos - Generalista/Multidisciplina	1	0.002065



 3  Localización Ciudad                                48431 non-null  str   
            a la hora de verlo vemos que sao paula y varias ciudades mas estan escritas de varias formas, por lo que los datos no son fidedignos
            hay que cambiar en el eda la ciudades sie es necesario


 4  Subactividad_desc  no hay nulos

            Cantidad  Porcentaje (%)
            Subactividad_desc                                                           
            fuerzadeventasdirecta                                   7503       15.492143
            instalaciónymantenimientoreddeacceso(redexterna)        5973       12.333010
            canaltelefónico-atención                                5418       11.187050
            ingenieríayconstruccióndeinfraestructurasderedt...      3416        7.053334
            operacióndered                                          2129        4.395945
            callcentertécnico                                       2107        4.350519
            producciónit                                            1999        4.127522
            operacionesredparaempresas                              1967        4.061448
            backoffice                                              1861        3.842580
            canaltelefónico-comercial                               1836        3.790960
            ingenieríayconstruccióndeinfraestructurasderedd...      1457        3.008404
            soporteventas                                           1037        2.141191
            fuerzadeventasindirecta                                  896        1.850055
            mantenimientoredtroncal(redinterna)                      752        1.552724
            soportedered                                             747        1.542401
            planificacióneinteligenciadelnegocio                     722        1.490781
            marketingdecliente(ofertacomercial,captaciónyfi...       690        1.424707
            marketingdeproducto(diseñoydesarrollodeproducto...       641        1.323532
            tecnologíayplanificación                                 614        1.267783
            pre-ventas                                               568        1.172803
            supervisióndered                                         565        1.166608
            calidadyoptimizacióndeprocesos                           511        1.055109
            planificaciónycontrolling                                476        0.982842
            desarrollodeproyectosestratégicosytransformación         421        0.869278
            aplicaciones/desarrollo                                  415        0.856889
            aseguramientodeingresosycontroldefraude                  311        0.642151
            logísticadeterminalesyequipamientodecliente              307        0.633892
            asesoríalegalysoportejurídico                            269        0.555429
            administraciónygestióndecobros                           260        0.536846
            facturación                                              172        0.355144
            businesspartners                                         170        0.351015
            canalonlineydeautogestión-comercial                      146        0.301460
            formación                                                139        0.287006
            logísticadered                                           131        0.270488
            gestiónfiscalytributaria                                 125        0.258099
            compras                                                  124        0.256034
            contabilidad                                             123        0.253970
            relacioneslaboralesygestióndealiados                     114        0.235386
            gestiónymantenimientodeedificios                         113        0.233322
            intervenciónyauditoria                                   102        0.210609
            relacionesregulatoriasynormativas                         81        0.167248
            gestióndecontenidos                                       77        0.158989
            canalpresencial-comercialdistribuidorespecialis...        75        0.154859
            compensación,beneficiosymovilidadglobal                   74        0.152795
            gestióndelamorosidadeimpagos                              71        0.146600
            vigilanciayseguridad                                      65        0.134212
            canalonlineydeautogestión-atención                        57        0.117693
            administracióndelpersonal                                 56        0.115628
            selección                                                 54        0.111499
            estrategiacorporativa                                     51        0.105304
            marcaypublicidad(noinstitucional)                         46        0.094980
            relacionescongobiernoeinstituciones                       43        0.088786
            restodeserviciosgenerales                                 42        0.086721
            comunicación,culturaytransformación                       40        0.082592
            tesoreríayplanificaciónfinanciera                         35        0.072268
            gestióndeseguros                                          26        0.053685
            organización,planificaciónyreporting                      25        0.051620
            comunicaciones                                            25        0.051620
            talentoydesarrollo                                        21        0.043361
            gobiernoit                                                20        0.041296
            nómina                                                    18        0.037166
            responsabilidadsocialcorporativaypatrocinioscor...        17        0.035101
            gestióndelaoperadora                                      15        0.030972
            helpdesk                                                  14        0.028907
            mercadodecapitales                                        14        0.028907
            gestionydireccion                                          9        0.018583
            fusiones,adquisicionesyalianzas                            9        0.018583
            innovación                                                 8        0.016518
            apoyoalagestióndelaoperadora                               8        0.016518
            relaciónconinversores                                      8        0.016518


 5   Año                                                48431 non-null  int64  
    solo 2019     

 6   COD. UNIDAD DE NEGOCIO                             48431 non-null  int64     
    solo 2 codigos 156, 185
        185    32412 ---66.9%
        156    16019    33.0%

 7   Mes                                                48431 non-null  str   
    solo un mes julio

 8   Reducción de Jormada                               48431 non-null  str 
    No    99.044001
    Sí     0.955999       
    solo el 0.95% tiene  reduccion de jornada

 9   Tipo de contrato                                   48431 non-null  str 
    solo hay un tipo fijo          

 10  División                                           48431 non-null  str  
    los que llevan delante BRA es Brasil

                                                        Cantidad  Porcentaje (%)
                División                                                           
                BRA - VP Engenharia e Servicos ao Cliente     11434       23.608846
                OPERACIONES, RED Y TI                          9174       18.942413
                BRA - VP B2C                                   7563       15.616031
                BRA - VP Atendimento ao Cliente                6309       13.026780
                BRA - VP B2B e Atacado                         2685        5.543970
                CONSEJERA DELEGADA COO                         2152        4.443435
                BRA - VP Tecnologia Informacao                 1856        3.832256
                BRA - Chief Financial Officer                  1115        2.302244
                TERRITORIAL CENTRO Y SECTORES GGCC             1087        2.244430
                TERRITORIAL MEDITERRANEO                       1018        2.101959
                TERRITORIAL SUR                                 676        1.395800
                TERRITORIAL NORTE                               596        1.230617
                BRA - VP Pessoas                                537        1.108794
                FINANZAS Y CONTROL DE GESTION                   447        0.922963
                BRA - VP Dados e Inteligencia Artificial        272        0.561624
                SEGURIDAD Y PREVENCION DEL FRAUDE               255        0.526522
                BRA - VP Transformacao e Qualidade              244        0.503810
                ESTRATEGIA                                      241        0.497615
                BRA - VP Juridico                               212        0.437736
                RECURSOS HUMANOS                                164        0.338626
                BRA - VP Assuntos Regulatórios                  112        0.231257
                CALIDAD Y TRANSFORMACION                         97        0.200285
                BRA - Presidencia                                72        0.148665
                ...
                AUDITORIA, INSPECCION E INTERVENCION             20        0.041296
                VIDEO ESPAÑA                                     12        0.024778
                DESARROLLO DE NEGOCIO MULTIMARCA                  9        0.018583
                BRA_VP de Relacoes Institucionais                 1        0.002065


 11  Subactividad                                       48431 non-null  str     
    da exactamente lo mismo que subactividad_des, columna copiada     

 12  Género                                             48431 non-null  str      
    M    63.07 %
    F    36.93 %

 13  Departamento                                       47986 non-null  str   
        gente que trabaja por departamento
                                            Cantidad  Porcentaje (%)
            Departamento                                                       
            OPERACIONES                                    4927           10.17
            SOPORTE Y EXPL. RED,SERVICIOS Y SISTEMAS       1488            3.07
            POSTVENTA                                      1360            2.81
            EMPRESAS                                       1251            2.58
            ESTRAT. Y DESARR. DE RED E INFRAESTR. TI        922            1.90
            GRAN PUBLICO Y PYMES SUR                        452            0.93
            NaN                                             445            0.92
            GRAN PUBLICO CENTRO                             410            0.85
            GRAN PUBLICO MEDITERRANEO                       352            0.73
            GRAN PUBLICO                                    345            0.71
            GGCC Y EMPRESAS ESTE                            295            0.61
            GGCC Y EMPRESAS CATALUÑA                        262            0.54
            DESARROLLO DE SISTEMAS                          255            0.53
            PEQUEÑA Y MEDIANA PRESENCIAL CENTRO             235            0.49
            FINANZAS, RIESGO Y COBROS                       230            0.47
            EMPRESAS NORTE                                  206            0.43
            SEGURIDAD DIGITAL                               205            0.42
            CANALES ON LINE                                 164            0.34
            FACTURACION, SOPORTE E IMPLANT. TELCO           158            0.33
            GRAN PUBLICO NORTE                              152            0.31
            CHIEF DATA OFFICER TE                           146            0.30
            MAYORISTA                                       124            0.26
            BRA_Ger Suporte Operacoes 12                    120            0.25
            ...
            BRA_Dir Inovacao e Novos Negocios                 1            0.00
            BRA_Ger Sr Desenvolvimento de Produtos            1            0.00
            BRA_Ger Sr Gestao de Produto                      1            0.00
            BRA_Ger Sr Serv Financ e Seguros                  1            0.00



 14  HORAS TEÓRICAS SEMANALES POR UNIDAD DE NEGOCIO     48431 non-null  float64 
     solo hay 2 posibles 
     España es    37.5
     Brasil es    44.

 15  Nombre del puesto                                  48431 non-null  str      

            Cantidad  Porcentaje (%)
            Nombre del puesto                                                      
            OPERADOR DE COMUNICACIONES                         4049            8.36
            TITULADO/TECNICO MEDIO O DE GRADO                  2552            5.27
            ASESOR COMERCIAL                                   1323            2.73
            TITULADO SUPERIOR O MASTER                         1221            2.52
            INSTALADOR LA                                      1204            2.49
            ENCARGADO DE OPERACION                             1117            2.31
            CONSULTOR NEGOCIOS LOJA I 6H                       1011            2.09
            Consultor Negocios Loja I                           978            2.02
            REPARADOR LA                                        905            1.87
            Atendente Retencao                                  848            1.75
            ADMINISTRATIVO                                      762            1.57
            ATENDENTE RETENCAO                                  579            1.20
            COORDINADOR                                         576            1.19
            JEFE                                                564            1.16
            ATENDENTE DE AGENDAMENTO E CONTROLE                 548            1.13
            Instalador La                                       540            1.11
            ASSISTENTE TECNICO                                  527            1.09
            CONSULTOR NEGOCIOS LOJA I                           515            1.06
            Atendente Telemarketing                             504            1.04
            ATENDENTE CO                                        448            0.93
            Reparador La                                        445            0.92
            ATENDENTE FIXA PLATINUM                             402            0.83
            Assistente Tecnico                                  398            0.82
            ...
            ANALISTA PROCESSOS EFICIENCIA PL                      1            0.00
            Gerente Processos e Eficiencia                        1            0.00
            Analista Projetos SR                                  1            0.00
            Diretor Presidente                                    1            0.00



 16  Nacionalidad                                       16019 non-null  str        
    solo aparece española con 16019
    pero 32412 son nulos 
    hay que ver cuantos son brasileños se puede sacar por columna localizacion pais
    si damos por echo que todos los que trabajan en Brasil son nacionalizados brasileños

 17  Estado de empleado                                 48431 non-null  str       
    solo hay 1 activo 

 18  PROMEDIO DE HORAS  SEMANALES TRABAJADAS EN EL MES  48431 non-null  float64       

            Cantidad  Porcentaje (%)
            PROMEDIO DE HORAS  SEMANALES TRABAJADAS EN EL MES                          
            40.0                                                  16369           33.80
            37.5                                                  15556           32.12
            44.0                                                   9249           19.10
            36.0                                                   6802           14.04
            32.8                                                    146            0.30
            34.5                                                     63            0.13
            25.0                                                     44            0.09
            35.0                                                     39            0.08
            34.3                                                     34            0.07
            36.5                                                     17            0.04
            37.0                                                     17            0.04
            20.0                                                     15            0.03
            33.6                                                     14            0.03
            29.6                                                     13            0.03
            35.5                                                      8            0.02
            22.5                                                      6            0.01
            24.7                                                      5            0.01
            29.4                                                      4            0.01
            0.4                                                       3            0.01
            34.0                                                      3            0.01
            18.8                                                      3            0.01
            1.5                                                       2            0.00
            35.4                                                      2            0.00
            ...
            22.3                                                      1            0.00
            28.2                                                      1            0.00
            28.0                                                      1            0.00
            28.4                                                      1            0.00



 19  Fecha de Nacimiento                                48431 non-null  datetime64[us]
        formato AAAA/MM/DD

 20  Clase de empleado                                  48431 non-null  str   
                Cantidad  Porcentaje (%)
                Clase de empleado                          
                EMP                   48420           99.98
                PRA                       8            0.02
                INP                       3            0.01
                

 21  Discapacidad                                       48431 non-null  str    
                              Cantidad  Porcentaje (%)
                Discapacidad                          
                No               47978           99.06
                Sí                 453            0.94

 22  Fecha de Alta                                      48431 non-null  datetime64[us]
          formato AAAA/MM/DD

 23  ID persona   
        pone `persona y numero  ---- Persona 1716852
        empieza en el numero 'Persona 1403121'
        termnina en el numero 'Persona 1732870'

      




# df_bajas_agosto ( solo estan las bajas de agosto)

                RangeIndex: 360 entries, 0 to 359
                Data columns (total 12 columns):
                #   Column                  Non-Null Count  Dtype         
                ---  ------                  --------------  -----         
                0   ID persona              360 non-null    str    
                        pone `persona y numero  ---- Persona 1716852 eliminar la palabra persona y espacio dejar solo el numero 

                1   Unidad de Negocio       360 non-null    str   
                
                            Cantidad	Porcentaje (%)
                    Unidad de Negocio		
                    Brasil	354	98.33
                    España	6	1.67


                2   COD. UNIDAD DE NEGOCIO  360 non-null    int64  

                            Cantidad	Porcentaje (%)
                    COD.		
                    185	           354	    98.33
                    156	             6	     1.67 

                3   Subactividad_desc       360 non-null    str  

                
                                                     Cantidad	        Porcentaje (%)
                       		
                        callcentertécnico	        97	26.94
                        canaltelefónico-atención    35	9.72
                        supervisióndered	        32	8.89
                        gestióndelamorosidadeimpagos19	5.28
                        fuerzadeventasdirecta	    17	4.72
                        operacióndered	            14	3.89
                        producciónit	            12	3.33
                        planificaciónycontrolling	11	3.06
                        relacioneslaboralesygestióndealiados	11	3.06
                        selección	                10	2.78
                        contabilidad	             9	2.50
                        gestióndeseguros	         9	2.50
                        formación	                 7	1.94
                        administraciónygestióndecobros	6	1.67
                        ingenieríayconstruccióndeinfraestructurasdereddeacceso	6	1.67
                        intervenciónyauditoria	      5	1.39
                        compensación,beneficiosymovilidadglobal	5	1.39
                        talentoydesarrollo	        5	1.39
                        tecnologíayplanificación	4	1.11
                        tesoreríayplanificaciónfinanciera	4	1.11
                        relaciónconinversores	    4	1.11
                        restodeserviciosgenerales	4	1.11
                        relacionescongobiernoeinstituciones	4	1.11
                        compras                 	3	0.83
                        gestiónfiscalytributaria	3	0.83
                        facturación	                3	0.83
                        calidadyoptimizacióndeprocesos	3	0.83
                        aseguramientodeingresosycontroldefraude	3	0.83
                        aplicaciones/desarrollo	    3	0.83
                        vigilanciayseguridad	    2	0.56
                        gestiónymantenimientodeedificios	2	0.56
                        mercadodecapitales	        2	0.56
                        asesoríalegalysoportejurídico	2	0.56
                        gestionydireccion	        1	0.28
                        organización,planificaciónyreporting	1	0.28
                        mantenimientoredtroncal(redinterna)	1	0.28
                        soporteventas	            1	0.28
         
                4   Subactividad            360 non-null    str  


                                        
                                                        Cantidad	Porcentaje (%)
                        Subactividad		
                        Call Center técnico	                97	26.94
                        Canal telefónico - Atención	        35	9.72
                        Supervisión de red	                32	8.89
                        Gestión de la morosidad e Impagos	19	5.28
                        Fuerza de ventas directa	        17	4.72
                        Operación de red	                14	3.89
                        Producción IT	                    12	3.33
                        Planificación y controlling	        11	3.06
                        Relaciones Laborales y Gestión de Aliados	11	3.06
                        Selección	                        10	2.78
                        Contabilidad	                    9	2.50
                        Gestión de Seguros	                9	2.50
                        Formación	                        7	1.94
                        Administración y gestión de cobros	6	1.67
                        Ingeniería y construcción de infraestructuras de Red de Acceso	                            6	1.67
                        Intervención y Auditoria	        5	1.39
                        Compensación, Beneficios y Movilidad Global	5	1.39
                        Talento y Desarrollo	            5	1.39
                        Tecnología y Planificación      	4	1.11
                        Tesorería y planificación financiera	4	1.11
                        Relación con Inversores	            4	1.11
                        Resto de servicios generales       	4	1.11
                        Relaciones con gobierno e instituciones	4	1.11
                        Compras	                            3	0.83
                        Gestión fiscal y tributaria     	3	0.83
                        Facturación	                        3	0.83
                        Calidad y Optimización de procesos	3	0.83
                        Aseguramiento de ingresos y control de fraude	3	0.83
                        Aplicaciones/Desarrollo	            3	0.83
                        Vigilancia y Seguridad	            2	0.56
                        Gestión y mantenimiento de edificios	2	0.56
                        Mercado de Capitales	            2	0.56
                        Asesoría legal y soporte jurídico	2	0.56
                        Gestión y Direccion	                1	0.28
                        Organización, Planificación y Reporting	1	0.28
                        Mantenimiento Red Troncal (Red Interna)	1	0.28
                        Soporte ventas	1	0.28
         
                5   Genero                  360 non-null    str   

                        
                        Cantidad	Porcentaje (%)
                    Genero		
                    M	    210	        58.33
                    F	    150	        41.67


                6   Fecha nacimiento        360 non-null    datetime64[us]
                    Formato AAAA/MM/DD

                7   Fecha fin de contrato   360 non-null    datetime64[us]
                    Formato AAAA/MM/DD

                8   Tipo de baja local      360 non-null    str 
                    
                                                        Cantidad	Porcentaje (%)
                    Tipo de baja local		
                    Dispensa sem Justa Causa AVP Inden.	       265         	73.61
                    Pedido Demissão	                            54	        15.00
                    Dispensa Com Justa Causa	                16	         4.44
                    Pedido Dem na Experiência	                10	         2.78
                    Antes Termino Contrato	                     7         	 1.94
                    b.1) Renuncias voluntarias	                 4	         1.11
                    b.2) Otras bajas vegetativas	             2           0.56
                    Falecimento morte natural	                 2	         0.56


                9   Clase de empleado       360 non-null    str  
                    solo hay una clase EMP         

                10  Tipo de baja global     360 non-null    str   
                	                                        Cantidad	Porcentaje (%)
                    Tipo de baja global		
                    a.2 ) X otras causas (Indemnizaciones)	    290	    80.56
                    b.1) Renuncias voluntarias	                 68    	18.89
                    b.2) Otras bajas vegetativas	              2    	0.56      


                11  Nombre del puesto       360 non-null    str     

                
                                                        Cantidad	Porcentaje (%)
                    Nombre del puesto		
                    ATENDENTE EXPERIENCIA CLIENTE II	45	12.50
                    ATENDENTE RETENCAO	                22	6.11
                    CONSULTOR NEGOCIOS LOJA I	        20	5.56
                    CONSULTOR NEGOCIOS LOJA I 6H	    17	4.72
                    INSTALADOR LA	                    14	3.89
                    REPARADOR LA	                    12	3.33
                    CONSULTOR NEGOCIOS LOJA 8H	        12	3.33
                    ASSISTENTE TECNICO	                12	3.33
                    ATENDENTE EXPERIENCIA CLIENTE I	     9	2.50
                    ATENDENTE TELEVENDAS I	             8	2.22
                    ATENDENTE EXPERIENCIA CLIENTE III	 7	1.94
                    AUXILIAR LA	                         7	1.94
                    ATENDENTE CO	                     7	1.94
                    RECEPCIONISTA LOJA	                 7	1.94
                    CONSULTOR RELACIONAMENTO LOJA	     7	1.94
                    SUPERVISOR SERVICOS AO CLIENTE	     7	1.94
                    ATENDENTE DE AGENDAMENTO E CONTROLE	 6	1.67
                    CONSULTOR NEGOCIOS LOJA I (NOC)	     5	1.39
                    GERENTE NEGOCIOS II               	 4	1.11
                    TECNICO TELECOM JR	                 4	1.11
                    ASSISTENTE ADMINISTRATIVO	         4	1.11
                    TITULADO SUPERIOR O MASTER	         3	0.83
                    ANALISTA TELECOM JR	                 3	0.83
                    CONSULTOR NEGOCIOS PREMIUM	         3	0.83
                    CONSULTOR SISTEMAS	                 3	0.83
                    GERENTE VENDAS B2C	                 3	0.83
                    CONSULTOR TECNOLOGICO	             3	0.83
                    GERENTE NEGOCIOS LOJA I	             3	0.83
                    ANALISTA SUPORTE VENDAS PL	         3	0.83
                    GERENTE GERAL LOJA II	             3	0.83
                    ENGENHEIRO TELECOM SR	             2	0.56
                    GERENTE CONTAS III	                 2	0.56
                    GERENTE GERAL LOJA I	             2	0.56
                    ANALISTA EXPERIENCIA CLIENTE SR    	 2	0.56
                    ANALISTA SUPORTE COMERCIAL I (OC)	 2	0.56
                    GERENTE CONTAS I	                 2	0.56
                    ANALISTA SUPORTE OPERACAO PL	     2	0.56
                    ATENDENTE TELEVENDAS III	         2	0.56
                    ATENDENTE RETENCAO VENDAS	         2	0.56
                    CONSULTOR SUPORTE OPERACAO	         2	0.56
                    GERENTE NEGOCIOS IS I	             2	0.56
                    CONSULTOR PRODUCAO TI	             2	0.56
                    GER SR CONTROLE OPERACOES FIN	     2	0.56
                    GERENTE NEGOCIOS III	             2	0.56
                    CONSULTOR MARKETING	                 2	0.56
                    CONSULTOR PROJETOS	                 2	0.56
                    TITULADO/TECNICO MEDIO O DE GRADO	 1	0.28
                    EXPERTO NIVEL 2	                     1	0.28
                    STAM	                             1	0.28
                    SUPERVISOR ATENDIMENTO OPERACOES	 1	0.28
                    ANALISTA SISTEMAS SR	             1	0.28
                    GERENTE NEGOCIOS LOJA (ITIN)	     1	0.28
                    ANALISTA CONTABIL SR	             1	0.28
                    ANALISTA RELACIONAMENTO COM CLIENTE SR	1	0.28
                    CONSULTOR CREDITO	                 1	0.28
                    ATENDENTE TELEMARKETING SME	         1	0.28
                    CONSULTOR GESTÃO DE PESSOAS	         1	0.28
                    CONSULTOR NEGOCIOS PREMIUM 6H	     1	0.28
                    ANALISTA GESTAO VENDAS PL	         1	0.28
                    ANALISTA LOGISTICA PL	             1	0.28
                    CONSULTOR VENDAS	                 1	0.28
                    ESPECIALISTA PLANEJAMENTO COMERCIAL	 1	0.28
                    ANALISTA PLANEJAMENTO COMERCIAL SR	 1	0.28
                    GERENTE MARKETING	                 1	0.28
                    GERENTE NEGOCIOS V	                 1	0.28
                    COORDENADOR SUPORTE SISTEMAS	     1	0.28
                    CONSULTOR SUPORTE	                 1	0.28
                    ANALISTA SISTEMAS JR	             1	0.28
                    GER SR PROCESSOS FINANCEIROS	     1	0.28
                    CONSULTOR PLANEJAMENTO E CONTROLE	 1	0.28
                    COORDENADOR SERVICO AO CLIENTE	     1	0.28
                    ANALISTA CONTROLE OPER FINANCEIRAS SR	1	0.28
                    ANALISTA SERVICO CLIENTE SR        	1	0.28
                    CONSULTOR BIG DATA	                1	0.28
                    LIGADOR DG	                        1	0.28
                    SUPERVISOR SUPORTE VENDAS	        1	0.28
                    ANALISTA SUPORTE COMERCIAL III	    1	0.28
                    AUDITOR JR	                        1	0.28
                    COORDENADOR ADMINISTRATIVO	        1	0.28
                    ASSISTENTE RELACIONAMENTO ODC	    1	0.28
                    ANALISTA SUPORTE VENDAS JR	        1	0.28
                    CONSULTOR TELECOM	                1	0.28
                    CONSULTOR LOGISTICA	                1	0.28
                    CONSULTOR PRE VENDAS IV	            1	0.28
                    ADVOGADO SR	                        1	0.28
                    SUPERVISOR RETENCAO I	            1	0.28
                    ANALISTA MARKETING PL	            1	0.28
                    CONSULTOR CONTABILIDADE	            1	0.28
                    ANALISTA QUALIDADE OPERACIONAL JR	1	0.28
                    SUPERVISOR ATENDIMENTO	            1	0.28
                    ANALISTA SEGURANCA PATRIMONIAL SR	1	0.28
                    TECNICO TELECOM SR	                1	0.28
                    SUPERVISOR TELEVENDAS I	            1	0.28
                    ENGENHEIRO TELECOM PL	            1	0.28
                    GERENTE RELAC POS VENDAS III	    1	0.28
                    ANALISTA CANAIS DIGITAIS SR	        1	0.28
                    TRAINEE	                            1	0.28
                    ANALISTA PLANEJAMENTO E CONTROLE PL	1	0.28
                    ANALISTA SUPORTE COMERCIAL I	    1	0.28
                    ANALISTA MARKETING SR	            1	0.28
                    GERENTE CONTAS IV	                1	0.28
                    GERENTE NEGOCIOS LOJA	            1	0.28
                    ATENDENTE COE PL	                1	0.28
                    TECNICO ADSL	                    1	0.28
                    DIR INSPECAO	                    1	0.28
                    ANALISTA PROJETOS SR	            1	0.28
                    ATENDENTE RELACIONAMENTO ODC	    1	0.28
                    GERENTE NEGOCIOS LOJA II	        1  	0.28
                    CONSULTOR INFRAESTRUTURA PREDIAL	1	0.28
                    ANALISTA PROCESSOS OPERACIONAIS PL	1	0.28
                    ANALISTA GESTAO VENDAS SR	        1	0.28


df_altas_agosto (solo estan las altas de agosto)

EDa
JULIO :

9   Tipo de contrato                                   48431 non-null  str 
    solo hay un tipo fijo     
    no aporta nada pq solo hay un tipo se puede eliminar esta columna

 3  Localización Ciudad                                48431 non-null  str   
            a la hora de verlo vemos que sao paula y varias ciudades mas estan escritas de varias formas, por lo que los datos no son fidedignos
            hay que cambiar en el eda la ciudades sie es necesario

 11  Subactividad                                       48431 non-null  str     
    da exactamente lo mismo que subactividad_des, columna copiada eliminar una de las 2


 17  Estado de empleado                                 48431 non-null  str       
    solo hay 1 activo  no tiene sentido, eliminar columna


 23  ID persona   
        pone `persona y numero  ---- Persona 1716852 eliminar la palabra persona y espacio dejar solo el numero 

BAJAS :

0   ID persona              360 non-null    str    
                        pone `persona y numero  ---- Persona 1716852 eliminar la palabra persona y espacio dejar solo el numero 

 9   Clase de empleado       360 non-null    str  
                    solo hay una clase EMP
                    eliminar columna