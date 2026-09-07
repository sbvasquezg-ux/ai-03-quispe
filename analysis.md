# Reconstrucción y crítica del modelo

Todas las páginas citadas son páginas físicas del PDF de arXiv v2. Cuando difieren, indico también la página impresa.

## 1. Problema del agente

El paper no escribe un único programa global. Como no hay una restricción que conecte lenguajes, su problema separable puede reconstruirse, para cada desarrollador (i), lenguaje (k) y mes (t), como

\[
m^g_{ikt}\in\arg\max_{m\in M_g\cup\{\varnothing\}}
\{V^m_{ikt},0\},\qquad
M_1=\{S,C\},\quad M_2=\{S,C,D\}.
\]

La alternativa exterior \(\varnothing\) paga cero. El lenguaje está activo si

\[
V^g_{ikt}=\max_{m\in M_g}V^m_{ikt}\ge 0,
\qquad Z^g_{ikt}=\mathbf 1\{V^g_{ikt}\ge0\},
\qquad N^g_{it}=\sum_k Z^g_{ikt}.
\]

Los excedentes de certeza equivalente son (sección 4.1, PDF pp. 13-14, impresas 11-12):

\[
\begin{aligned}
V^S&=\omega+s\mu-\frac{\rho s^2}{2\pi}-b,\\
V^C&=V^S+\gamma s-r_C,\\
V^D&=\omega+(1-\lambda)s\mu+\lambda a z(A)-\kappa(a,s)-r_D-b
-\frac{\rho}{2}\left[\frac{(1-\lambda)^2s^2}{\pi}+\sigma_D^2(a,s,A)\right].
\end{aligned}
\]

La variable de elección es discreta: modo de producción o no entrada. No se eligen endógenamente (s,a,A,\lambda) ni los costos. La formulación tampoco incluye una restricción de tiempo, presupuesto o atención entre lenguajes.

### Primitivas y dominios

- (k\in\{1,\ldots,K\}), (i) desarrollador, (t) mes; conjuntos familiar (K_i) y no familiar (U_i), con (U_i=|U_i|).
- (s_{ikt}\in[0,1]), habilidad específica; (a_i\ge0), habilidad general.
- (\theta_{ik}\sim N(\mu_{ikt},1/\pi_{ikt})), por lo que (\mu\in\mathbb R) y la precisión requiere (\pi>0).
- (\rho>0), coeficiente CARA; (\lambda\in(0,1]), fracción delegada.
- (\omega_{ikt}), valor de oportunidad; (b_{ikt}), costo de activación; (r_C,r_D), costos de interacción/cómputo; (A), capacidad del agente; (z(A)), competencia creciente; (\kappa(a,s)), costo de verificación; (\sigma_D^2(a,s,A)\ge0), varianza residual.
- El texto llama “costos” a (b,r_C,r_D,\kappa), pero no declara allí dominios formales para todos ellos, ni dominio o cotas para (A,\gamma,z,\omega,\mu). Esa omisión impide tratar sus signos como supuestos escritos.

### Supuestos numerados

1. **Assumption 1 (Augmentation requires a foothold).** Para un lenguaje no familiar, \(\gamma s-r_C\le0\); para uno familiar con habilidad \(\bar s\), \(\gamma\bar s-r_C>0\) (sección 4.1, PDF p. 14).
2. **Assumption 2 (Verification technology).** \(\kappa_a<0\), \(\kappa_s\le0\), \(\partial_a\sigma_D^2\le0\), \(\partial_s\sigma_D^2\le0\) y \(\partial_A\sigma_D^2\le0\) (sección 4.1, PDF p. 14).
3. **Assumption 3 (Comparable unfamiliar-language candidates).** Condicional en características del desarrollador, todos los lenguajes no familiares tienen el mismo incremento de activación (p_i(a_i,A)\ge0), creciente en (a_i) cuando el Supuesto 2 hace caer los umbrales con habilidad (apéndice A.5, PDF p. 62, impresa 60).

## 2. Decisión que separa el modelo de ALZ

La hipótesis propuesta se confirma, con una precisión. En Aouad, Lykouris y Zhong la elección continua de esfuerzo satisface (x=s+e+a): skill, esfuerzo y asistencia son sustitutos perfectos en el margen intensivo. Aquí la elección central es el modo discreto y la entrada de cada lenguaje. Los umbrales (sección 4.2, PDF pp. 14-15) son

\[
T^S=b-s\mu+\frac{\rho s^2}{2\pi},\qquad
T^1=T^S-\max\{0,\gamma s-r_C\},
\]

\[
T^D=b-(1-\lambda)s\mu-\lambda az(A)+\kappa+r_D
+\frac{\rho}{2}\left[\frac{(1-\lambda)^2s^2}{\pi}+\sigma_D^2\right],
\qquad T^2=\min\{T^1,T^D\}.
\]

Para un lenguaje no familiar, el Supuesto 1 fuerza (T^1=T^S). La ecuación decisiva es

\[
Z^2-Z^1=\mathbf1\{T^D\le\omega<T^S\}
\quad\text{si }B\equiv T^S-T^D>0.
\]

Por tanto, la innovación no consiste solo en añadir asistencia a una tecnología continua. Añade un modo al menú y abre un margen extensivo. La precisión importante es que (V^D) también sustituye ejecución humana, modifica riesgo e introduce verificación. El mecanismo estructural es una nueva tecnología de producción. Su representación observable se reduce, sin embargo, a mover un umbral.

## 3. Objeción A: el umbral no identifica agencia

La ventaja de delegación es (ecuación 7, sección 4.2, PDF p. 15)

\[
B=\lambda[az(A)-s\mu]-\kappa(a,s)-r_D
+\frac{\rho}{2}\left[\frac{(2\lambda-\lambda^2)s^2}{\pi}-\sigma_D^2(a,s,A)\right].
\]

La “agencia” mueve varios términos: reemplaza la fracción \(\lambda\) de ejecución, añade (az(A)), reduce exposición al riesgo del match humano, y añade verificación, cómputo y error residual. No es literalmente una reducción exógena de (b). Pero, una vez colapsado a la decisión de entrada, todo opera mediante el escalar (B).

### Modelo rival

Sea (q\ge0) una mejora genérica: documentación, chat, un colega o una librería reduce el costo efectivo de entrada a (b-q). Manteniendo el modo pre-agente,

\[
\widetilde T=T^S-q,\qquad
\widetilde Z-Z^1=\mathbf1\{T^S-q\le\omega<T^S\}.
\]

Si (F) tiene densidad (f),

\[
P(\widetilde Z-Z^1=1)=F(T^S)-F(T^S-q),\qquad
\frac{\partial P}{\partial q}=f(T^S-q)\ge0.
\]

Para (U_i) candidatos simétricos, (E[\widetilde N-N^1]=U_i[F(T^S)-F(T^S-q)]). Al elegir (q=B), el rival produce exactamente la misma banda, probabilidad de entrada, mayor efecto entre especialistas y dinámica de primeras entradas que el modelo agéntico. Incluso las comparativas en (a,s,A) se replican dejando (q=q(a,s,A)).

El modelo sí contiene estructura específicamente agéntica en los componentes de (B), pero los outcomes usados solo observan la forma reducida del umbral. Para discriminar hacen falta restricciones que el rival no pueda copiar: variación experimental entre chat y agente con el mismo modelo base; medición de la fracción ejecutada (\lambda); tareas donde el agente pueda actuar pero documentación o chat no cambien; o predicciones distintas sobre verificación, errores y tiempo humano.

Excluir commits con trailer de Claude no resuelve esta equivalencia. El efecto en commits “no asistidos” es 1.663 lenguajes en (e=0), frente a 2.528 en todos los commits (tabla 4, PDF p. 39). Eso rechaza que todo el resultado sea depósito mecánico de archivos firmados por Claude, pero admite tres lecturas: aprendizaje/complementariedad, asistencia sin trailer y shock de proyecto. No hay contradicción lógica porque el apéndice A.7 añade aprendizaje como canal secundario (PDF pp. 64-65). Sí hay una tensión interpretativa: cuanto más peso recibe el output no firmado, menos identifica el dato la delegación contemporánea que define el modelo central.

## 4. Objeción B: frontera o selección

### Selección en tendencias

El paper sí estima pre-trends de los outcomes relevantes. El conteo mensual y el flujo de lenguajes nuevos muestran coeficientes planos antes de (e=-1) (sección 7.1 y figuras 2-3, PDF pp. 31-32). Pero el stock acumulado, la predicción dinámica de la Proposición 3, falla el diagnóstico: cuatro de cinco coeficientes pretratamiento son significativos (sección 7.3, PDF p. 33). Además, actividad y uso de lenguajes suben en (e=-1), un “reversed Ashenfelter dip” compatible con un nuevo proyecto (sección 10.4, PDF p. 52). Permitir un mes de anticipación evita usarlo como pre-periodo, pero no vuelve exógeno el timing.

### Reversión a la media y headroom

Los especialistas tienen, por construcción, más lenguajes que todavía pueden aparecer como “nuevos”. El doble ordenamiento por volumen y breadth compara celdas de actividad semejante y encuentra efectos mayores en especialistas (sección 9, tabla 7, PDF pp. 45-49), pero no elimina el límite inferior ni el agotamiento del conjunto en riesgo. La propia variable “nuevo” usa historia observable solo desde enero de 2024 (nota 4, PDF p. 22), de modo que baja actividad previa también crea falsa novedad. Un test más limpio estimaría, entre no adoptantes emparejados por actividad y breadth, la tasa esperada de descubrimiento de nuevos lenguajes y usaría como outcome el exceso sobre esa tasa; mejor aún, asignaría aleatoriamente acceso a agente versus chat y estratificaría ex ante por breadth. También conviene usar historia completa o una ventana común larga y mostrar resultados por distancia al techo factible.

### Contaminación mecánica

La amenaza YAML/JSON/TOML no sobrevive tal como está formulada. Linguist excluye markup, data y prose, incluido JSON y YAML, y aplica reglas path-based para vendored, generated y documentation (sección 5.3, PDF p. 22). Dockerfile y Makefile sí cuentan como lenguajes por reglas de filename, y lockfiles pueden heredar clasificación según extensión. Excluir los lenguajes introducidos por el primer commit de Claude reduce el ATT de lenguajes de 2.528 a 1.580 y el de nuevos de 1.193 a 0.807 (tabla 3, PDF p. 37): la contaminación inmediata es material, aunque no explica todo lo medido.

### Porosidad de la exclusión

La regla elimina commits cuyo mensaje contiene el trailer `Co-Authored-By: Claude`. No identifica quién escribió líneas dentro de un commit firmado por el humano. El paper reconoce que history rewrites pueden quitar trailers y llama al panel “unassisted” una aproximación (sección 8.2, PDF pp. 38-39). También reconoce que herramientas sin trazas, como autocomplete de Copilot o Cursor, son invisibles (sección 5.2, PDF p. 21). Por ello, “sin coautoría detectable” es correcto; “código escrito sin agente” no está identificado.

### Contrafactuales

Sí hay not-yet-treated: adoptantes de 2025Q4-2026Q1 sirven de control antes de adoptar (sección 5.2, PDF pp. 19-20), y el estimador Callaway-Sant’Anna usa comparaciones cohort-time con un mes de anticipación (sección 6.1, PDF pp. 25-26). También hay un placebo temporal doce meses antes con ceros precisos (sección 8.6, PDF p. 44). No hay placebo de modalidad con asignación o adopción de una herramienta conversacional comparable. La afirmación de que Generación 1 era universalmente accesible no equivale a observar uso ni intensidad.

El diseño que falta asignaría aleatoriamente, sobre el mismo modelo y precio, chat versus agente, o explotaría una regla exógena de elegibilidad. El paper propone rollouts regionales, cambios de precio o umbrales de suscripción institucional (sección 10.6, PDF pp. 52-53).

**Veredicto causal.** Sobrevive la afirmación descriptiva: entre adoptantes sostenidos, la primera coautoría detectable de Claude coincide con un aumento grande y transitorio de breadth y primeras apariciones, parte del cual persiste en commits sin trailer. No sobrevive “Claude Code causó la expansión” ni “la delegación, y no un shock de proyecto o productividad, fue el mecanismo”. El enunciado más fuerte defendible es el del propio cierre del paper: asociación de event time, robusta a varias contaminaciones observables y cuantitativamente consistente con el modelo, sin identificación causal ni de mecanismo (sección 10.7, PDF p. 53).

## 5. Objeción C: endpoints

- **Igualdad en activación.** Como (Z=\mathbf1\{V\ge0\}), (\omega=T^D) activa bajo delegación y pertenece a la banda; (\omega=T^S) ya activa solo y queda fuera. La banda correcta es ([T^D,T^S)) (Proposición 2, PDF p. 15).
- **(B=0).** Da (T^D=T^S), banda vacía y cero expansión. La condición estricta (B>0) en la Proposición 2 es necesaria.
- **Banda de medida cero.** Aun con (B>0), (F(T^S)-F(T^D)) puede ser cero si la distribución no tiene masa en ese intervalo. Continuidad de (F) no implica densidad positiva. La proposición solo promete probabilidad y expansión esperada débiles, así que no falla; una lectura de expansión estricta requeriría soporte positivo.
- **Menú inicial unitario.** Si solo existe un lenguaje y ya está activo, la Proposición 1 sigue dando igualdad. Si (U_i=0), las sumas de las Proposiciones 3 y 4 valen cero: cualquier conclusión estricta agregada necesita no-vacuidad.
- **(\lambda=0).** El paper lo excluye: (\lambda\in(0,1]). El límite no reproduce automáticamente trabajo solo, porque quedan (\kappa,r_D,\sigma_D^2). Identificar “sin agencia” con (\lambda=0) exige además anular esos términos.
- **(\lambda=1).** Delegación total elimina la media y varianza del match humano, pero (B=az(A)-s\mu-\kappa-r_D+\frac\rho2(s^2/\pi-\sigma_D^2)); no garantiza (B>0). Más agencia no implica entrada sin restricciones adicionales.
- **Hazards iguales.** Si (p^2=p^1), la fórmula de la Proposición 3 es cero y satisface solo la conclusión débil.
- **Endpoint (p^2=1).** El hazard es una probabilidad y el dominio impreso admite 1. Con (U_i=\{k\}), (p^1_{ik}=0), (p^2_{ik}=1),
  \[
  \Delta C_i(s)=1^{s+1}-0^{s+1}=1\quad(s\ge0).
  \]
  No crece ni es estrictamente cóncava. Este es el contraejemplo numérico mínimo. El paso inválido está en el apéndice A.6: afirma (p^2(1-p^2)^{s+1}>0), falso en (p^2=1) (PDF p. 64, impresa 62). Es un supuesto faltante, probablemente un descuido de endpoint: el resultado estricto se repara con (U_i\ne\varnothing) y (0<p^2_{ik}<1) para al menos un término relevante. La fórmula débil sigue correcta.

## 6. Trabajo propio

`sim.py` implementa el modelo rival, comprueba la equivalencia reducida (q=B), recorre casos límite y produce `simulation.csv`. La simulación muestra una lección adicional: el ancho (B) no determina por sí solo la expansión esperada; la masa de oportunidades dentro de la banda sí.

