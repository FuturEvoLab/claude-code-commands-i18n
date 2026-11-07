# Comandos de Claude Code

[English](README.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-Hant.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Español](README.es.md)

![Unofficial](https://img.shields.io/badge/Anthropic-unofficial-lightgrey) [![check](https://github.com/FuturEvoLab/claude-code-commands-i18n/actions/workflows/check.yml/badge.svg)](https://github.com/FuturEvoLab/claude-code-commands-i18n/actions/workflows/check.yml) [![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-blue)](LICENSE-CONTENT) [![Code: MIT](https://img.shields.io/badge/code-MIT-green)](LICENSE) ![Commands](https://img.shields.io/badge/commands-115-teal)

> Una referencia no oficial y en lenguaje sencillo de todos los comandos de barra de Claude Code, en **7 idiomas: inglés, japonés, chino simplificado, chino tradicional, coreano, ruso y español**. Está pensada para quienes encuentran difícil leer la documentación oficial en inglés: cada comando tiene el significado de su palabra en inglés, una explicación breve y un ejemplo realista de cuándo usarlo.

## Vista previa en vivo

Una página estática que puedes probar ya: busca, cambia de idioma y de tema y copia comandos. No hay nada que instalar.

### [Versión web con búsqueda →](https://futurevolab.github.io/claude-code-commands-i18n/)

| Tema predeterminado | Tema Matrix |
|---|---|
| [![Tema predeterminado](docs/assets/preview-en.png)](https://futurevolab.github.io/claude-code-commands-i18n/?theme=terminal) | [![Tema Matrix](docs/assets/preview-matrix.png)](https://futurevolab.github.io/claude-code-commands-i18n/?theme=matrix) |

<p><img src="docs/assets/preview-search.png" alt="search" width="68%"> <img src="docs/assets/preview-mobile.png" alt="mobile" width="28%"></p>

## Cómo leer la sintaxis

- Escribe `/` en el prompt para abrir el menú de comandos; sigue escribiendo para filtrar.
- `[ ]` = opcional, `< >` = obligatorio, `|` = elegir una de las opciones. Puedes escribir los argumentos en español.
- **Habilidad** = un prompt incluido que se le entrega a Claude. **Flujo de trabajo** = ejecuta varios agentes en segundo plano.
- Muchos comandos dependen de la versión, el plan, la plataforma o de que una función esté activada. El menú que ves es el que vale; comprueba tu versión con `/status`.

## ★ Empieza aquí

La selección del editor para tu primera semana con Claude Code.

- `/clear` · Empezar una conversación nueva (la anterior se puede retomar)
- `/compact` · Resumir una conversación larga para liberar espacio
- `/context` · Ver qué está llenando la ventana de contexto
- `/plan` · Ver primero un plan; los cambios esperan tu aprobación
- `/resume` · Volver a una conversación anterior
- `/rewind` · Deshacer: volver atrás el código y la conversación
- `/model` · Cambiar de modelo
- `/init` · Crear el CLAUDE.md del proyecto
- `/code-review` · Buscar errores antes del commit y, si quieres, corregirlos
- `/loop` · Repetir un prompt cada cierto tiempo
- `/mcp` · Gestionar conexiones con herramientas externas
- `/permissions` · Decidir qué puede hacer Claude sin preguntar
- `/usage` · Ver el costo y los límites del plan
- `/doctor` · Hacer un chequeo cuando algo falla
- `/help` · Ver la ayuda y todos los comandos
- `/powerup` · Aprender funciones con lecciones interactivas

## Busca un comando según lo que quieres hacer

Elige la situación; los comandos aparecen en el orden en que conviene probarlos.

- **Claude rompió algo y quiero deshacerlo** → `/rewind` · `/diff`
- **Empezar desde cero una tarea sin relación** → `/clear` · `/resume`
- **La conversación es larga y Claude va lento u olvida cosas** → `/context` · `/compact` · `/autocompact`
- **Continuar el trabajo que dejé sin terminar ayer** → `/resume` · `/rename` · `/recap`
- **Ver un plan antes de un cambio grande** → `/plan` · `/effort` · `/model`
- **Hacer que Claude responda siempre en mi idioma** → `/init` · `/memory`
- **Gastar menos dinero y consumir menos uso** → `/usage` · `/model` · `/effort` · `/context`
- **Revisar el trabajo antes de hacer commit o de publicarlo** → `/diff` · `/code-review` · `/security-review` · `/verify`
- **Hacer varias cosas a la vez o trabajar en segundo plano** → `/fork` · `/subtask` · `/background` · `/tasks` · `/batch`
- **Repetir una tarea o ejecutarla según un horario** → `/loop` · `/schedule` · `/goal`
- **Demasiadas solicitudes de permiso** → `/permissions` · `/fewer-permission-prompts`
- **Conectar herramientas o añadir nuevas capacidades** → `/mcp` · `/plugin` · `/skills`
- **Crear diapositivas, diseños o gráficos** → `/slides` · `/design` · `/dataviz` · `/artifacts`
- **Dejar el equipo y seguir en el teléfono** → `/remote-control` · `/mobile` · `/desktop`
- **El propio Claude Code funciona mal** → `/doctor` · `/status` · `/debug` · `/bug`
- **Aprender Claude Code a fondo** → `/powerup` · `/help` · `/insights`

## Etiquetas de seguridad

Los comandos marcados con estas etiquetas requieren especial cuidado.

- **¥ Puede costar dinero**: Puede consumir uso de pago o generar cargos extra. Revisa primero `/usage` y los precios oficiales.
- **↗ Envía datos fuera**: Envía la conversación, el código o comentarios a otro servicio (Anthropic, GitHub, sesiones en la nube, sitios abiertos en tu navegador) o hace push a un remoto. Comprueba primero qué se envía y adónde.
- **⚿ Puede exponer secretos**: La salida (archivos, portapapeles, informes) puede contener texto de la conversación, claves, contraseñas o datos personales. Revísala y elimina lo sensible antes de compartirla.
- **⇄ Cambios amplios en archivos**: Puede cambiar o revertir muchos archivos a la vez. Haz commit o una copia de seguridad antes, y revisa con `/diff` después.
- **⚑ Cambia la configuración de seguridad**: Cambia lo que Claude puede hacer sin preguntar u otras opciones de seguridad. Permite solo acciones que entiendas y en las que confíes.

## Contenido

- [Conversación y contexto](#conversación-y-contexto) (15)
- [Modelo y razonamiento](#modelo-y-razonamiento) (5)
- [Proyecto y archivos](#proyecto-y-archivos) (7)
- [Revisión y verificación](#revisión-y-verificación) (7)
- [Trabajo en paralelo y en segundo plano](#trabajo-en-paralelo-y-en-segundo-plano) (10)
- [Automatización y programación](#automatización-y-programación) (4)
- [Artefactos, diapositivas y diseño](#artefactos-diapositivas-y-diseño) (9)
- [Complementos, habilidades e integraciones](#complementos-habilidades-e-integraciones) (13)
- [Permisos y seguridad](#permisos-y-seguridad) (7)
- [Configuración e interfaz](#configuración-e-interfaz) (10)
- [Cuenta y uso](#cuenta-y-uso) (8)
- [Nube, acceso remoto y otros dispositivos](#nube-acceso-remoto-y-otros-dispositivos) (8)
- [Diagnóstico y comentarios](#diagnóstico-y-comentarios) (10)
- [Otros](#otros) (2)
- [Eliminados](#eliminados) (3)

## Conversación y contexto

Empezar, compactar, rebobinar y retomar conversaciones; gestionar la ventana de contexto

| Comando | Palabra en inglés | Qué hace | Mejor uso |
|---|---|---|---|
| `/clear`<br>`[name]`<br>★ | clear<br>borrar, limpiar | Empieza una conversación nueva con el contexto vacío, pero conserva la memoria del proyecto. La conversación anterior se guarda y puedes volver a abrirla con `/resume`; si escribes un nombre, sirve de etiqueta en el selector.<br>Alias: `/reset`, `/new` | Cuando terminas una función y pasas a una tarea sin relación: `/clear funcion-de-inicio-de-sesion`. El contexto viejo deja de interferir y el uso baja. |
| `/compact`<br>`[instructions]`<br>★ | compact<br>compactar, resumir | Resume la conversación hasta ahora para liberar espacio de contexto y sigue en la misma conversación. Puedes añadir instrucciones para indicar qué debe conservar el resumen. | Después de una sesión larga: `/compact conserva el esquema de la base de datos y la lista de errores pendientes`. |
| `/context`<br>`[all]`<br>★ | context<br>contexto (lo que Claude «recuerda» ahora) | Muestra el uso del contexto como una cuadrícula de colores, con sugerencias para optimizar y avisos de capacidad. `all` muestra el desglose por elemento. | Cuando Claude parece olvidar cosas o el uso sube rápido, ejecuta `/context` para ver si archivos grandes o la salida de herramientas están llenando la ventana. |
| `/plan`<br>`[description]`<br>★ | plan<br>plan | Entra en el modo plan: Claude investiga y propone un plan antes de editar. Si añades una descripción, empieza esa tarea de inmediato. | Antes de un cambio grande: `/plan corrige el error de autenticación`, revisa y luego aprueba. |
| `/resume`<br>`[session]`<br>★ | resume<br>reanudar | Retoma una conversación por su ID o nombre, o abre el selector de sesiones. Las sesiones en segundo plano aparecen marcadas con `bg`.<br>Alias: `/continue` | Ayer cerraste el portátil a mitad de una tarea: `/resume` y elige la conversación de ayer. |
| `/rewind`<br>★ · ⇄ Cambios amplios en archivos | rewind<br>rebobinar | Devuelve la conversación, el código o ambos a un punto de control anterior, o resume a partir de un mensaje que elijas.<br>Alias: `/checkpoint`, `/undo` | Claude rompió varios archivos: ejecuta `/rewind`, elige el mensaje anterior a los cambios y restaura el código y la conversación. |
| `/autocompact`<br>`[auto\|<tokens>]`<br>Requiere v2.1.221+ | auto compact<br>compactación automática | Define cuánto se llena la ventana de contexto antes de la compactación automática, por ejemplo `500k`; `auto` vuelve al valor predeterminado ajustado al modelo. Se guarda en la configuración de usuario y se aplica al momento. | Una tarea larga se interrumpe por compactaciones frecuentes: `/autocompact 500k`. |
| `/branch`<br>`[name]` | branch<br>rama, bifurcación | Crea una rama de la conversación en este punto y cambia a ella; la original se conserva y puedes volver con `/resume`. (Es una rama de la conversación, no una rama de Git). | Dudas entre dos enfoques: `/branch probar-plan-b`; si no funciona, vuelve atrás y sigue con el plan A. |
| `/btw`<br>`[question]` | by the way<br>por cierto | Hace una pregunta aparte sobre la sesión actual sin añadirla a la conversación. Sin pregunta, muestra tu última pregunta aparte. | En medio de una tarea quieres entender un error: `/btw qué significa este 404`, sin desviar el hilo principal. |
| `/copy`<br>`[N]` | copy<br>copiar | Copia la última respuesta al portapapeles; `/copy 2` copia la penúltima. Si hay bloques de código, un selector te deja copiar uno solo; pulsa `w` para escribirlo en un archivo (útil por SSH). | Claude escribió un fragmento de código o un comando: `/copy` y pégalo donde lo necesites. |
| `/export`<br>`[filename]`<br>⚿ Puede exponer secretos | export<br>exportar | Exporta la conversación como texto plano: directamente a un archivo si le das un nombre o, si no, mediante un diálogo para copiar o guardar. | Para archivar una sesión de depuración valiosa: `/export notas-de-depuracion.txt`. |
| `/goal`<br>`[condition\|clear]` | goal<br>objetivo, meta | Fija un objetivo: Claude sigue trabajando turno tras turno hasta que se cumple la condición o se borra el objetivo. Sin argumento, muestra el objetivo actual; `clear` (o `stop`, `off`, …) lo elimina. | `/goal todas las pruebas pasan`, y deja que itere hasta que todo esté en verde. |
| `/memory` | memory<br>memoria | Edita los archivos de memoria `CLAUDE.md`, activa o desactiva la memoria automática y muestra sus entradas. | Quieres que todas las respuestas estén en tu idioma: abre `/memory` y añade una línea como «Responde siempre en español». |
| `/recap` | recap<br>recapitular, resumen | Genera cuando lo pides un resumen de una línea de la sesión actual. | Vuelves de una reunión y perdiste el hilo: `/recap`. |
| `/rename`<br>`[name]` | rename<br>renombrar | Cambia el nombre de la sesión y lo muestra en la barra del prompt; sin nombre, genera uno a partir de la conversación. | Con muchas sesiones abiertas: `/rename backtest` para que destaque en `/resume`. |

## Modelo y razonamiento

Cambiar de modelo, el esfuerzo de razonamiento y la velocidad

| Comando | Palabra en inglés | Qué hace | Mejor uso |
|---|---|---|---|
| `/model`<br>`[model]`<br>★ | model<br>modelo | Cambia de modelo y lo guarda como predeterminado para las sesiones nuevas. Sin argumento abre un selector; las flechas izquierda/derecha ajustan el esfuerzo en los modelos compatibles; pulsa `s` en una fila para cambiar solo en esta sesión. | Usa un modelo más rápido para cambios pequeños; cambia con `/model opus` cuando un error se complica. |
| `/advisor`<br>`[model\|off]` | advisor<br>asesor | Activa o desactiva la herramienta de asesor, que consulta a un segundo modelo en los momentos clave. Acepta `fable`, `opus`, `sonnet` o un ID de modelo completo (`fable` requiere acceso). Sin argumento abre un selector. | Trabaja con un modelo más rápido, pero recibe una segunda opinión más potente en las decisiones clave: `/advisor opus`. |
| `/effort`<br>`[level\|auto\|status\|ultracode [on\|off]]` | effort<br>esfuerzo (profundidad del razonamiento) | Define el nivel de esfuerzo: de `low` a `xhigh`, `max` o `auto`; `status` lo muestra. `max` vale solo para la sesión. `ultracode on\|off` activa o desactiva ultracode. | Para cazar un error intermitente: `/effort high`; para corregir una errata: `/effort low`. |
| `/fast`<br>`[on\|off]` | fast<br>rápido | Activa o desactiva el modo rápido (mismo modelo, salida más rápida). Puedes cambiarlo en medio de una respuesta; el turno en curso termina a su velocidad original. Consulta la documentación oficial del modo rápido para ver los precios. | Si tienes prisa: `/fast on`; si no, `/fast off`. |
| `/output-style`<br>`[style]`<br>Requiere v2.1.269+ | output style<br>estilo de salida | Muestra los estilos de salida o cambia a uno, por ejemplo `/output-style concise`. | Ejecuta `/output-style` sin argumento para ver qué hay disponible y luego elige uno (por ejemplo, un estilo más conciso). |

## Proyecto y archivos

Configurar la memoria del proyecto, añadir carpetas, revisar cambios

| Comando | Palabra en inglés | Qué hace | Mejor uso |
|---|---|---|---|
| `/init`<br>★ | initialize<br>inicializar | Inicializa el proyecto con una guía `CLAUDE.md` que lee cada sesión nueva. Ofrece `/import` si encuentra configuración de Codex o Gemini CLI. | Lo primero en un repositorio nuevo: `/init`, y luego mejóralo con `/memory`. |
| `/add-dir`<br>`<path>` | add directory<br>añadir carpeta | Añade una carpeta de trabajo para acceder a sus archivos en esta sesión, sin moverte. Las rutas parciales se autocompletan con `Tab`. La mayor parte de la configuración `.claude/` de la carpeta añadida no se detecta, y la mayoría de las rutas de red no se pueden añadir. | El frontend y el backend están uno al lado del otro: `/add-dir ../backend`. |
| `/cd`<br>`<path>` | change directory<br>cambiar de carpeta | Mueve la sesión a otra carpeta de trabajo y conserva la conversación. A diferencia de `/add-dir`, `/cd` cambia el lugar donde vive la sesión. | Empezaste en la carpeta equivocada: `/cd ~/projects/website` en lugar de empezar de nuevo. |
| `/diff` | difference<br>diferencia | Revisa los cambios de tu árbol de trabajo, incluidos los que Claude ha hecho hasta ahora. | Antes de hacer commit, `/diff` para ver exactamente qué cambió. |
| `/import`<br>`[codex\|gemini\|cursor] [--dry-run] [--yes]`<br>⇄ Cambios amplios en archivos | import<br>importar | Importa archivos de instrucciones, servidores MCP, comandos, subagentes y habilidades de OpenAI Codex, Gemini CLI o Cursor. `--dry-run` muestra una vista previa. No está disponible en algunos proveedores en la nube; importar desde Cursor requiere v2.1.265 o posterior. | Si vienes de Cursor: primero `/import cursor --dry-run` y después importa de verdad. |
| `/insights` | insights<br>ideas, análisis | Genera un informe HTML de tus sesiones recientes en este equipo: proyectos, hábitos, dónde fallan las cosas y funciones que vale la pena probar. No está disponible en sesiones en la nube. | Después de unas semanas, ejecuta `/insights` para descubrir funciones que nunca probaste. |
| `/team-onboarding`<br>⚿ Puede exponer secretos | team onboarding<br>incorporación al equipo | Analiza tus sesiones, comandos y uso de MCP de los últimos 30 días y escribe una guía en Markdown que un compañero puede pegar como su primer mensaje. | Llega alguien nuevo al equipo: ejecuta `/team-onboarding` y envíale la guía. |

## Revisión y verificación

Encontrar errores y vulnerabilidades, limpiar el código, ejecutar la aplicación para verificar

| Comando | Palabra en inglés | Qué hace | Mejor uso |
|---|---|---|---|
| `/code-review`<br>`[low\|medium\|high\|xhigh\|max\|ultra] [--fix] [--comment] [--max-findings n\|all\|default] [pr#\|branch\|path]`<br>★ · Habilidad · ¥ Puede costar dinero · ↗ Envía datos fuera · ⇄ Cambios amplios en archivos | code review<br>revisión de código | Revisa el diff actual, o un PR, una rama o una ruta, en busca de errores de funcionamiento. `--fix` aplica las correcciones, `--comment` publica en el PR de GitHub o el MR de GitLab, `ultra` hace una revisión profunda en la nube.<br>Alias: `/review` | Antes de hacer commit: `/code-review high --fix`. Para un PR: `/code-review high 1234`. |
| `/run`<br>Habilidad | run<br>ejecutar | Inicia y maneja la aplicación de tu proyecto para ver un cambio funcionando. | `/run` para arrancar el sitio y hacer una captura de la nueva página de inicio. |
| `/run-skill-generator`<br>Habilidad | skill generator<br>generador de habilidades | Escribe una habilidad propia del proyecto que enseña a `/run` y `/verify` a compilar, iniciar y manejar tu aplicación desde un entorno limpio. | El arranque necesita varios pasos (primero la base de datos, etc.): ejecútalo una vez y después `/run` funciona sin más. |
| `/security-review` | security review<br>revisión de seguridad | Analiza el diff de tu rama frente a la rama predeterminada de origin en busca de vulnerabilidades como inyección, problemas de autenticación o exposición de datos. Necesita un remoto `origin`. | Antes de publicar algo que toque autenticación, pagos o datos de usuarios. |
| `/simplify`<br>`[target]`<br>Habilidad · ⇄ Cambios amplios en archivos | simplify<br>simplificar | Cuatro agentes en paralelo revisan el código cambiado buscando reutilización, simplificación, eficiencia y nivel de abstracción, y luego aplican las correcciones. No busca errores de funcionamiento; para eso usa `/code-review`. | La función ya funciona y quieres un código más limpio: `/simplify`. |
| `/ultrareview`<br>`[PR or branch]`<br>¥ Puede costar dinero | ultra review<br>revisión ultra | Revisión profunda con varios agentes en un sandbox en la nube. La forma preferida es `/code-review ultra`; `/ultrareview` es un alias. Incluye 3 ejecuciones gratis en Pro, Max y Ultra; después requiere créditos de uso. | Antes de una versión importante: `/code-review ultra`. |
| `/verify`<br>Habilidad | verify<br>verificar | Compila, ejecuta y observa tu aplicación para confirmar que un cambio funciona, en lugar de fiarse de las pruebas o de la comprobación de tipos. Solo se ejecuta cuando lo invocas. | Cambiaste el comportamiento de un botón: `/verify` para que de verdad haga clic en él. |

## Trabajo en paralelo y en segundo plano

Ejecutar varios agentes a la vez o pasar trabajo a segundo plano

| Comando | Palabra en inglés | Qué hace | Mejor uso |
|---|---|---|---|
| `/agents` | agents<br>agentes | Muestra un recordatorio de que puedes pedirle a Claude que cree o gestione subagentes, o editar `.claude/agents/` directamente. En v2.1.197 y anteriores abría un gestor interactivo. | Simplemente pídelo: «Crea un subagente que solo escriba pruebas». |
| `/background`<br>`[prompt]` | background<br>segundo plano | Separa la sesión para que siga como agente en segundo plano y libera la terminal. Opcionalmente, antes envía una instrucción más. Síguela con `claude agents`.<br>Alias: `/bg` | Un trabajo de 30 minutos: `/bg escribe los resultados en report.md cuando termines`. |
| `/batch`<br>`<instruction>`<br>Habilidad · ⇄ Cambios amplios en archivos | batch<br>lote | Coordina cambios grandes en paralelo: investiga el código, divide el trabajo en 5–30 unidades independientes y presenta un plan; tras tu aprobación, un subagente en segundo plano por unidad la implementa y la prueba en su propio worktree. Requiere un repositorio git o un hook WorktreeCreate. | `/batch migra src/ de JavaScript a TypeScript`. |
| `/fork`<br>`[prompt]` | fork<br>bifurcar (copia) | Copia la conversación en una sesión nueva en segundo plano mientras tú sigues trabajando aquí. Con un prompt, la copia empieza de inmediato; normalmente se le indica que primero cree su propio worktree. | Trabajas en la función A y quieres una corrección aparte en paralelo: `/fork corrige la alineación del pie de página`. |
| `/list-agents`<br>Requiere v2.1.224+ | list agents<br>lista de agentes | Lista los subagentes, compañeros y otras sesiones a los que Claude puede enviar mensajes, con el nombre que debes usar para cada uno. Solo donde los mensajes entre sesiones están activados.<br>Alias: `/peers` | Si coordinas varias sesiones: comprueba cómo se llama cada una. |
| `/stop` | stop<br>detener | Detiene la sesión en segundo plano a la que estás conectado; la transcripción y el worktree se conservan. Para desconectarte sin detenerla, usa `/exit` o pulsa `←`. | Un trabajo en segundo plano se desvió: `/stop`. |
| `/subtask`<br>`<task>` | subtask<br>subtarea | Lanza un subagente bifurcado que hereda la conversación y devuelve su resultado aquí. La diferencia con `/fork`: `/subtask` devuelve el resultado aquí, mientras que `/fork` crea una sesión aparte. | `/subtask documenta estos endpoints de la API` mientras sigues programando. |
| `/tasks` | tasks<br>tareas | Muestra y gestiona el trabajo en segundo plano de esta sesión, incluidos los subagentes que ya terminaron.<br>Alias: `/bashes` | Mira el avance de pruebas o subagentes en segundo plano con `/tasks`. |
| `/workflow-authoring`<br>Habilidad | workflow authoring<br>creación de flujos de trabajo | Carga la referencia para escribir scripts de flujos de trabajo dinámicos. Claude normalmente la carga solo; ejecútalo antes de editar a mano un script guardado. Solo donde los flujos de trabajo dinámicos están activados. | Antes de editar a mano un script de flujo de trabajo guardado. |
| `/workflows` | workflows<br>flujos de trabajo | Abre la vista de progreso de flujos de trabajo para ver, pausar, reanudar o guardar flujos en curso y terminados. | Vigila un flujo de trabajo que tarda mucho. |

## Automatización y programación

Repetir cada cierto tiempo, ejecutar según un horario, corregir pull requests automáticamente

| Comando | Palabra en inglés | Qué hace | Mejor uso |
|---|---|---|---|
| `/loop`<br>`[interval] [prompt]`<br>★ · Habilidad | loop<br>bucle, repetir | Ejecuta un prompt una y otra vez mientras la sesión sigue abierta. Si omites el intervalo, Claude marca su propio ritmo; si omites el prompt, ejecuta el prompt de mantenimiento integrado o tu `loop.md`.<br>Alias: `/proactive` | `/loop 5m comprueba si terminó el despliegue`. Para ejecuciones que sigan con el equipo apagado, usa `/schedule`. |
| `/autofix-pr`<br>`[prompt]`<br>↗ Envía datos fuera | auto-fix PR<br>corrección automática de PR | Lanza una sesión en la nube que vigila el PR de la rama actual y sube correcciones cuando falla la CI o hay comentarios de revisión. Requiere la CLI `gh` y sesiones en la nube. | `/autofix-pr corrige solo errores de lint y de tipos`. |
| `/deep-research`<br>`<question>`<br>Flujo de trabajo | deep research<br>investigación a fondo | Un flujo de trabajo incluido que lanza muchas búsquedas web, obtiene y contrasta fuentes y escribe un informe con citas. Se ejecuta en segundo plano. | `/deep-research compara precios y calidad de las principales herramientas de video con IA`. |
| `/schedule`<br>`[description]` | schedule<br>programar | Crea, actualiza, lista o ejecuta tareas programadas en la nube (antes llamadas rutinas) mediante una conversación guiada. No está disponible con una clave de API de Console.<br>Alias: `/routines` | `/schedule cada día laborable a las 9, resume los issues nuevos del repositorio`. |

## Artefactos, diapositivas y diseño

Crear páginas, presentaciones, diseños y gráficos para compartir

| Comando | Palabra en inglés | Qué hace | Mejor uso |
|---|---|---|---|
| `/artifact-capabilities`<br>Habilidad | artifact capabilities<br>capacidades de artefactos | Carga la referencia de las capacidades de ejecución de los artefactos, como llamar a conectores u ofrecer descargas, y cuáles tiene tu cuenta. Claude normalmente la carga solo. | Antes de crear una página que mucha gente va a rellenar. |
| `/artifact-diagramming`<br>Habilidad · Requiere v2.1.221+ | artifact diagramming<br>diagramas para artefactos | Carga una guía de diagramas para artefactos: cuándo ayuda un diagrama, qué dibujar y SVG que se lee bien en temas claros y oscuros. | Cuando necesitas un diagrama de arquitectura claro. |
| `/artifacts` | artifacts<br>artefactos (páginas publicadas) | Lista los artefactos que te pertenecen o que otros comparten contigo, y luego conecta uno, lo abre o copia su enlace. Donde los artefactos están disponibles. | Encuentra el panel de la semana pasada y sigue editándolo. |
| `/dataviz`<br>`[request]`<br>Habilidad | data visualization<br>visualización de datos | Guía para diseñar gráficos: elige el tipo de gráfico, asigna los colores según su función y valida la paleta (seguridad para daltonismo y contraste) con un script incluido. | `/dataviz convierte esta tabla de ventas mensuales en un gráfico de tendencia`. |
| `/design`<br>`[brief]`<br>Habilidad · Requiere v2.1.265+ | design<br>diseño | Crea bocetos de interfaz, flujos, páginas de aterrizaje o pósteres como mesas de trabajo en un solo lienzo (un artefacto de Claude Design); edítalos en un navegador de escritorio y expórtalos en PNG o PDF. No está disponible en Bedrock, Vertex ni otras plataformas de terceros. | `/design una pantalla de configuración para una app de banca móvil`. |
| `/design consent` | consent / revoke<br>consentimiento / revocar | Concede o retira el acceso de Claude a Claude Design. Cuando Claude te pida ejecutar `/design consent`, escríbelo tú mismo.<br>Alias: `/design revoke` | Cuando se te pida, escribe tú mismo `/design consent`. |
| `/design-login` | design login<br>inicio de sesión de diseño | Autoriza el acceso al sistema de diseño para `/design-sync` con tu cuenta de claude.ai, cuando `/design-sync` o `/design consent` te lo pidan. | Ejecútalo cuando `/design-sync` te pida iniciar sesión. |
| `/design-sync`<br>`[hint]`<br>Habilidad · ↗ Envía datos fuera | design sync<br>sincronización de diseño | Convierte y sube el sistema de diseño React de tu repositorio a Claude Design para que los diseños usen tus componentes reales. La primera sincronización puede tardar horas en repositorios grandes. Usa el sitio independiente claude.ai/design, que cierra a más tardar el 14 de diciembre de 2026. | `/design-sync Acme DS` (ten en cuenta la fecha de cierre indicada arriba). |
| `/slides`<br>`[brief]`<br>Habilidad · Requiere v2.1.265+ | slides<br>diapositivas | Crea un artefacto de Claude Slides a partir de tus indicaciones. Requiere una sesión con artefactos y una cuenta donde esté disponible la plantilla de Slides. | `/slides una revisión trimestral para la dirección, 8 diapositivas`. |

## Complementos, habilidades e integraciones

Ampliar Claude con complementos, habilidades, servidores MCP e integraciones con el navegador y el IDE

| Comando | Palabra en inglés | Qué hace | Mejor uso |
|---|---|---|---|
| `/mcp`<br>`[reconnect (<server>\|all)\|enable\|disable [<server>\|all]]`<br>★ | MCP (Model Context Protocol)<br>MCP (Model Context Protocol, estándar para conectar herramientas externas) | Gestiona las conexiones a servidores MCP y OAuth. Sin argumento abre la lista; `reconnect`, `enable` o `disable` con el nombre de un servidor o `all` actúan directamente. | Un conector falló o necesita autenticación: `/mcp reconnect all`. |
| `/chrome` | Chrome<br>navegador Chrome | Configura los ajustes de Claude in Chrome. | Al conectar la extensión de Chrome por primera vez. |
| `/claude-api`<br>`[subcommand]`<br>Habilidad | Claude API<br>API de Claude | Carga la referencia de la API de Claude y de Managed Agents para el lenguaje de tu proyecto; se activa sola cuando el código importa `anthropic`. Los subcomandos incluyen `migrate`, `upgrade`, `api-version`, `cost-optimize`, `latency-optimize`, `build-eval`, `prompt-audit`. | Reduce el gasto de API de tu aplicación: `/claude-api cost-optimize`. |
| `/claude-in-chrome`<br>`[task]`<br>Habilidad · ↗ Envía datos fuera | Claude in Chrome<br>Claude en Chrome | Hace que Claude realice una tarea en tu navegador mediante Claude in Chrome, como probar una página o leer los registros de la consola. Requiere la integración con Chrome (por ejemplo, `claude --chrome`). | `/claude-in-chrome prueba el registro de usuarios en mi sitio local e informa de los errores`. |
| `/ide` | IDE (integrated development environment)<br>IDE (entorno de desarrollo integrado, editor de código) | Gestiona las integraciones con IDE y muestra su estado. | Comprueba la conexión cuando los cambios no aparecen en tu editor. |
| `/install-github-app`<br>↗ Envía datos fuera · ⚑ Cambia la configuración de seguridad | install GitHub app<br>instalar la app de GitHub | Instala la Claude GitHub App en un repositorio y, si quieres, configura flujos de trabajo y secretos de GitHub Actions. Solo github.com. | Para mencionar a Claude en issues y PR y que trabaje ahí. |
| `/install-slack-app` | install Slack app<br>instalar la app de Slack | Instala la app de Claude para Slack mediante un flujo OAuth en el navegador. | Tu equipo quiere a Claude en Slack. |
| `/plugin`<br>`[subcommand]` | plugin<br>complemento (plugin) | Gestiona complementos. Sin argumento abre el menú; `list`, `install`, `enable`, `disable` actúan directamente. Ejecuta `/reload-plugins` si el resumen de instalación lo indica. | Explora con `/plugin` e instala uno que encaje con tu trabajo. |
| `/plugin-authoring`<br>Habilidad · Requiere v2.1.287+ | plugin authoring<br>creación de complementos | Carga la referencia para escribir un mod. Es una habilidad de un complemento integrado, que puedes desactivar en `/plugin`. | Cuando quieres un pequeño panel lateral que se quede junto al chat. |
| `/reload-plugins`<br>`[--force]` | reload plugins<br>recargar complementos | Recarga los complementos activos sin reiniciar e informa de los errores de carga. Si la recarga cambiaría las herramientas MCP cargadas e invalidaría la caché del prompt, avisa y no la hace salvo que pases `--force`. | Justo después de instalar un complemento que lo pide. |
| `/reload-skills` | reload skills<br>recargar habilidades | Vuelve a explorar las carpetas de habilidades y comandos para que las habilidades añadidas o cambiadas durante la sesión estén disponibles sin reiniciar. | Acabas de escribir una habilidad propia y la quieres usar ya. |
| `/skill-doctor`<br>Requiere v2.1.252+ | skill doctor<br>chequeo de habilidades | Muestra el costo de contexto y el uso de cada habilidad para que encuentres cuáles desactivar. | Ejecútalo de vez en cuando para quitar habilidades que no usas. |
| `/skills` | skills<br>habilidades | Lista las habilidades con filtros. `t` ordena por número de tokens, `Space`/`Enter` cambia la visibilidad de una habilidad para Claude y para el menú `/`, `Esc` guarda y cierra. | Demasiadas habilidades: `/skills`, pulsa `t` y oculta las pesadas que no usas. |

## Permisos y seguridad

Controlar qué puede hacer Claude y qué necesita tu aprobación

| Comando | Palabra en inglés | Qué hace | Mejor uso |
|---|---|---|---|
| `/permissions`<br>★ · ⚑ Cambia la configuración de seguridad | permissions<br>permisos | Gestiona las reglas de permitir, preguntar y denegar para las herramientas: verlas por ámbito, añadir o quitar reglas, gestionar carpetas de trabajo y revisar la pestaña Recently blocked (llamadas que frenó el modo automático) y las reglas del clasificador.<br>Alias: `/allowed-tools` | Te cansaste de aprobar `npm test` cada vez: permítelo aquí. |
| `/auto-mode-setup`<br>⚑ Cambia la configuración de seguridad | auto mode setup<br>configuración del modo automático | Redacta entradas de `autoMode.environment` a partir de tu proyecto y tus sesiones recientes para que las revises y guardes. Tiene requisitos de versión y de plan. | Cuando el modo automático bloquea una y otra vez acciones rutinarias. |
| `/fewer-permission-prompts`<br>Habilidad · ⚑ Cambia la configuración de seguridad | fewer permission prompts<br>menos solicitudes de permiso | Revisa las transcripciones en busca de llamadas comunes de solo lectura a Bash y MCP, y añade una lista de permitidos priorizada al `.claude/settings.json` del proyecto. | Ejecútalo una vez cuando las solicitudes de aprobación no dejan de interrumpirte. |
| `/hooks` | hooks<br>hooks (scripts que se ejecutan solos en momentos fijos) | Muestra la configuración de los hooks. | Revisa qué hay configurado cuando un hook parece romper cada cambio. |
| `/privacy-settings` | privacy settings<br>configuración de privacidad | Muestra y actualiza la configuración de privacidad. Solo Pro, Max y Ultra. | Para comprobar cómo se usan tus datos. |
| `/sandbox`<br>⚑ Cambia la configuración de seguridad | sandbox<br>sandbox (entorno aislado) | Activa o desactiva el modo sandbox, solo en plataformas compatibles. | Actívalo antes de ejecutar scripts que no conoces. |
| `/update-config`<br>`[request]`<br>Habilidad · ⚑ Cambia la configuración de seguridad | update config<br>actualizar la configuración | Describe un cambio de configuración (permitir un comando, definir una variable de entorno, añadir un hook) y Claude edita el `settings.json` correspondiente. Usa `/config` para el tema y el modelo. | `/update-config ejecuta prettier después de cada edición de archivo`. |

## Configuración e interfaz

Tema, colores, línea de estado, atajos de teclado, voz

| Comando | Palabra en inglés | Qué hace | Mejor uso |
|---|---|---|---|
| `/color`<br>`[color\|default]` | color<br>color | Define el color de la barra del prompt para esta sesión: `red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink` o `cyan`; `default` lo restablece y sin argumento elige un color al azar. | Marca una sesión de producción con `/color red`. |
| `/config`<br>`[key=value ...]` | config<br>configuración | Abre la configuración para el tema, el modelo, el estilo de salida y más, o define pares `key=value` directamente, por ejemplo `/config theme=dark`. `/config --help` lista las claves.<br>Alias: `/settings` | `/config theme=dark`. |
| `/focus` | focus<br>vista de enfoque | Activa o desactiva una vista que muestra solo tu último prompt, un resumen de una línea de las herramientas y la respuesta final. Solo con el renderizado a pantalla completa. | Oculta los pasos intermedios y ve solo el resultado. |
| `/keybindings` | keybindings<br>atajos de teclado | Abre tu archivo de atajos de teclado. | Asigna las acciones a las teclas que ya conoces. |
| `/scroll-speed` | scroll speed<br>velocidad de desplazamiento | Ajusta la velocidad de desplazamiento de la rueda del mouse. Solo con el renderizado a pantalla completa; no en la terminal de JetBrains. | Redúcela cuando un solo paso de la rueda salta demasiado. |
| `/statusline` | status line<br>línea de estado | Configura la línea de estado; describe lo que quieres o ejecútalo sin argumentos para basarla en el prompt de tu shell. | `/statusline muestra el modelo y la rama de git`. |
| `/terminal-setup` | terminal setup<br>configuración de la terminal | Instala Shift+Enter para saltos de línea en VS Code, Cursor, Devin Desktop, Alacritty o Zed; en Apple Terminal activa Option+Enter y desactiva la campana; en iTerm2 activa el acceso al portapapeles para `/copy`. | Enter envía prompts a medio escribir: ejecútalo una vez. |
| `/theme` | theme<br>tema | Cambia el tema de colores: `auto`, claro y oscuro, aptos para daltonismo, ANSI y temas personalizados. | Cambia a un tema oscuro por la noche. |
| `/tui`<br>`[default\|fullscreen]` | TUI (text user interface)<br>TUI (interfaz de usuario de texto) | Define el renderizador de la terminal y reinicia con la conversación intacta. `fullscreen` es el renderizador sin parpadeo. Sin argumento, muestra el renderizador actual. | La pantalla parpadea: `/tui fullscreen`. |
| `/voice`<br>`[hold\|tap\|off]` | voice<br>voz | Activa o desactiva el dictado por voz o elige un modo (`hold`, `tap`). Requiere una cuenta de Claude.ai. | Dicta instrucciones en lugar de escribirlas. |

## Cuenta y uso

Iniciar sesión, revisar límites y costos, mejorar el plan

| Comando | Palabra en inglés | Qué hace | Mejor uso |
|---|---|---|---|
| `/usage`<br>★ | usage<br>uso | Muestra el costo de la sesión, el gasto de hoy, de esta semana y de este mes, los límites de uso del plan y estadísticas de actividad, incluido lo que cuenta para los límites del plan en las suscripciones. `/stats` abre la pestaña Stats. Cada aviso indica su causa y un arreglo de una línea; pulsa `f` para aplicar los arreglos.<br>Alias: `/cost`, `/stats` | Revisa `/usage` antes de decidir si cambias a un modelo más barato. |
| `/login` | log in<br>iniciar sesión | Inicia sesión en tu cuenta de Anthropic. | En un equipo nuevo o cuando la sesión caducó. |
| `/logout` | log out<br>cerrar sesión | Cierra la sesión de tu cuenta de Anthropic. | Después de usar un equipo compartido. |
| `/passes` | passes<br>pases de invitación | Comparte una semana gratis de Claude Code con amigos; solo aparece en cuentas que cumplen los requisitos. | Invita a un amigo a probarlo. |
| `/rate-limit-options` | rate limit options<br>opciones ante el límite de uso | Muestra formas de seguir trabajando cuando un límite de claude.ai te bloquea: esperar y continuar automáticamente, añadir créditos de uso o mejorar el plan. Requiere una suscripción a claude.ai. | El límite te bloqueó por la noche: elige continuar automáticamente cuando se restablezca. |
| `/status` | status<br>estado | Abre la configuración en la pestaña Status: versión, modelo, cuenta y conectividad. Funciona mientras Claude responde. | Haz una captura de `/status` antes de pedir ayuda. |
| `/upgrade` | upgrade<br>mejorar el plan | Abre la página para mejorar el plan en tu navegador. | Cuando llegas a los límites una y otra vez. |
| `/usage-credits`<br>¥ Puede costar dinero | usage credits<br>créditos de uso | Configura o solicita créditos de uso; los miembros de Team y Enterprise sin acceso a la facturación envían una solicitud a su administrador. Antes era `/extra-usage`. | Pide créditos a tu administrador cuando el equipo se queda sin ellos. |

## Nube, acceso remoto y otros dispositivos

Pasar el trabajo entre escritorio, móvil, web y nube

| Comando | Palabra en inglés | Qué hace | Mejor uso |
|---|---|---|---|
| `/desktop` | desktop<br>aplicación de escritorio | Continúa la sesión en la aplicación Claude Code Desktop. Requiere macOS o Windows x64 y una suscripción a Claude.<br>Alias: `/app` | Pasa de la terminal a la aplicación de escritorio. |
| `/mobile` | mobile<br>móvil | Muestra un código QR para descargar la aplicación móvil de Claude.<br>Alias: `/ios`, `/android` | Para seguir el trabajo desde tu teléfono. |
| `/remote-control`<br>↗ Envía datos fuera | remote control<br>control remoto | Hace que esta sesión esté disponible para Remote Control desde claude.ai. Requiere una suscripción a claude.ai.<br>Alias: `/rc` | Deja la tarea en marcha y dirígela desde tu teléfono: `/rc`. |
| `/remote-env` | remote environment<br>entorno remoto | Elige el entorno en la nube predeterminado para las sesiones en la nube iniciadas desde la CLI. | Elige uno predeterminado cuando tienes varios entornos. |
| `/setup-bedrock` | set up Bedrock<br>configurar Bedrock | Configura con un asistente la autenticación, la región y los modelos fijos de Amazon Bedrock. Está oculto en el menú hasta que se define `CLAUDE_CODE_USE_BEDROCK=1`; escríbelo completo. | Tu empresa usa Claude a través de AWS. |
| `/setup-vertex` | set up Vertex<br>configurar Vertex | Configura con un asistente Agent Platform de Google Cloud. Está oculto hasta que se define `CLAUDE_CODE_USE_VERTEX=1`; escríbelo completo. | Tu empresa usa Claude a través de Google Cloud. |
| `/teleport` | teleport<br>teletransportar | Trae una sesión en la nube a esta terminal, con su rama y su conversación. Requiere una suscripción a claude.ai.<br>Alias: `/tp` | Continúa en local una tarea que empezaste en la web. |
| `/web-setup` | web setup<br>configuración de la versión web | Conecta GitHub para las sesiones en la nube usando tus credenciales locales de `gh`. | Antes de tu primera sesión en la nube. |

## Diagnóstico y comentarios

Empieza aquí cuando algo falla

| Comando | Palabra en inglés | Qué hace | Mejor uso |
|---|---|---|---|
| `/doctor`<br>`[prompt-audit [path]]`<br>★ · Habilidad | doctor<br>médico (chequeo) | Hace un chequeo de la instalación, la configuración, las extensiones y `CLAUDE.md`, y propone correcciones que Claude aplica después de que confirmes. `prompt-audit` revisa en cambio tus instrucciones.<br>Alias: `/checkup` | Algo parece roto: empieza con `/doctor`. |
| `/help`<br>★ | help<br>ayuda | Muestra la ayuda y los comandos disponibles. | Olvidaste un comando: `/help`, o escribe `/` y unas letras. |
| `/powerup`<br>★ | power up<br>potenciar | Lecciones interactivas con demostraciones animadas que enseñan las funciones de Claude Code. | El mejor punto de partida estructurado para quien empieza. |
| `/bug`<br>`[report]`<br>↗ Envía datos fuera · ⚿ Puede exponer secretos | bug<br>error, fallo | Informa de un error o comparte tu conversación; tú eliges cuánto historial incluir y confirmas antes de que se envíe nada.<br>Alias: `/share` | Cuando el propio Claude Code se comporta mal. |
| `/debug`<br>`[description]`<br>Habilidad | debug<br>depurar | Activa el registro de depuración desde este momento y busca el problema leyendo el registro de depuración de la sesión. Opcionalmente, describe el problema. | `/debug el servidor MCP no logra conectarse`. |
| `/exit` | exit<br>salir | Sale de la CLI. En una sesión en segundo plano conectada, se desconecta y la sesión sigue en marcha.<br>Alias: `/quit` | Terminaste por hoy. |
| `/feedback`<br>`[report]`<br>↗ Envía datos fuera · ⚿ Puede exponer secretos | feedback<br>comentarios | Envía comentarios sobre el producto con el mismo diálogo y el mismo paso de consentimiento que `/bug`. | Pide una función nueva. |
| `/heapdump`<br>⚿ Puede exponer secretos | heap dump<br>volcado de heap (registro de la memoria) | Escribe en el Escritorio una instantánea del heap y un desglose de la memoria para diagnosticar un uso alto de memoria. Comparte solo el `-diagnostics.json`; el `.heapsnapshot` contiene tu conversación y tus credenciales. Está oculto en el menú. | Informa de un consumo de memoria descontrolado. |
| `/release-notes` | release notes<br>notas de la versión | Muestra el registro de cambios en un selector de versiones; las notas aparecen sin entrar en el contexto de Claude. | Mira qué hay de nuevo después de una actualización. |
| `/restart`<br>Requiere v2.1.288+ | restart<br>reiniciar | Reinicia Claude Code y retoma la sesión para aplicar una actualización instalada. Requiere Pro, Max o Ultra y una instalación nativa en macOS o Linux (no WSL).<br>Alias: `/update` | Cuando la barra inferior lo ofrece tras una actualización. |

## Otros

Pequeños extras

| Comando | Palabra en inglés | Qué hace | Mejor uso |
|---|---|---|---|
| `/radio` | radio<br>radio | Abre la radio lo-fi Claude FM en tu navegador o muestra la URL del stream. | Música de fondo mientras trabajas. |
| `/stickers` | stickers<br>stickers (pegatinas) | Pide stickers de Claude Code. | Decora tu portátil. |

## Eliminados

Aún aparecen en guías antiguas, pero ya no están disponibles

| Comando | Palabra en inglés | Qué hace | Mejor uso |
|---|---|---|---|
| `/pr-comments`<br>`[PR]`<br>Eliminado en v2.1.91 | PR comments<br>comentarios de PR | Eliminado en v2.1.91. Pídele a Claude directamente que muestre los comentarios del pull request. | Pídelo con tus propias palabras. |
| `/ultraplan`<br>`<prompt>` | ultra plan<br>plan ultra | Eliminado. Usa en su lugar el modo plan (`/plan`). | Usa `/plan`. |
| `/vim`<br>Eliminado en v2.1.92 | Vim<br>Vim (modo de edición centrado en el teclado) | Eliminado en v2.1.92. Usa `/config` → Editor mode. | Usa `/config`. |

## Aviso legal

1. **Proyecto no oficial**: Es un proyecto de la comunidad, sin relación con Anthropic y sin su patrocinio ni respaldo. «Claude», «Claude Code» y las marcas relacionadas son marcas comerciales de Anthropic y aquí se usan solo para identificar el producto descrito.
2. **Puede estar desactualizado o tener errores**: Cada descripción es una paráfrasis simplificada de la documentación oficial, ofrecida «tal cual», sin garantía de ningún tipo, ni expresa ni implícita. Claude Code cambia a menudo: se añaden, renombran y eliminan comandos. Si este proyecto y la documentación oficial no coinciden, manda la documentación oficial.
3. **Úsalo bajo tu propio riesgo**: Algunos comandos cambian o revierten archivos, ejecutan comandos, suben código, envían datos a servicios externos o consumen uso de pago. Entiende qué hace un comando antes de ejecutarlo, haz commit o una copia de seguridad antes, y no lo uses sin revisarlo en sistemas de producción, datos importantes o repositorios de otras personas.
4. **Protege tus secretos y tu privacidad**: No pongas en los prompts claves de API, contraseñas, tokens ni datos personales de otras personas. Las conversaciones exportadas, los informes de errores y las instantáneas de memoria pueden contenerlos; revísalos antes de compartirlos.
5. **Los ejemplos son ilustrativos**: Los ejemplos de «mejor uso» explican el propósito; no son instrucciones para tu entorno. La disponibilidad depende de la versión, el plan, la plataforma y las políticas de tu organización.
6. **Esta página no te rastrea**: Esta página no usa cookies, analítica, scripts ni fuentes de terceros. Solo guarda tus preferencias de idioma y tema, localmente en tu navegador.
7. **Limitación de responsabilidad**: En la máxima medida que permita la ley, los autores y colaboradores no son responsables de ninguna pérdida derivada del uso de este proyecto, incluidas la pérdida de datos, los cargos, los incidentes de seguridad o la interrupción del servicio.

## Sobre este proyecto

- **Fuente**: paráfrasis de la [referencia oficial de comandos](https://code.claude.com/docs/en/commands), revisada el 2026-11-07. Las descripciones están simplificadas y no son traducciones oficiales; si no coinciden, manda la documentación oficial.
- **Datos**: todo se genera a partir de [`data/commands.json`](data/commands.json). Edita el JSON y luego ejecuta `python3 scripts/build.py`.
- **Cómo colaborar**: consulta [CONTRIBUTING.md](CONTRIBUTING.md).
- **Licencia**: contenido [CC BY 4.0](LICENSE-CONTENT), código [MIT](LICENSE).
