# Catastro-Notificacion

Este repositorio contiene una solución para obtener actualizaciones periódicas sobre el avance del estado del Catastro Nacional Paraguayo y recibir notificaciones a través de Telegram, sin la necesidad de estar constantemente verificando la página.
Uso

Para utilizar este repositorio y recibir las notificaciones, es necesario especificar las siguientes variables de entorno:

    ANIO: El año del catastro que se desea monitorear.
    BOT_ID: El ID del bot de Telegram que enviará los mensajes.
    CHAT_ID: El ID del chat de Telegram donde se enviarán los mensajes.
    EXPEDIENTE_ID: El número de expediente del catastro que se desea monitorear.

## Ejecución

Este repositorio utiliza GitHub Actions para ejecutar la acción de notificación cada 5 horas. La acción se encargará de obtener el estado del catastro y enviar un mensaje a través de Telegram con la información actualizada.
Contribución

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes alguna sugerencia de mejora, por favor, abre un issue o envía un pull request.

## Aviso Legal

Este proyecto es solo con fines educativos y de demostración. No me responsabilizo del uso que se le pueda dar a la información obtenida a través de este repositorio.
## Licencia

Este proyecto está bajo la Licencia [MIT](https://opensource.org/licenses/MIT).
