from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from tasks.models import Task


@receiver(post_save, sender=Task)
def send_slack_notification(sender, instance, created, **kwargs):

    if created:
        user = instance.assigned_to

        if user:
            try:
                profile = user.profile
                slack_user_id = profile.slack_user_id

                client = WebClient(token=settings.SLACK_API_TOKEN)

                message = f"Se creó una nueva tarea para <@{user.username}>: {instance.subject}"

                response = client.chat_postMessage(
                    channel=slack_user_id,
                    text=message
                )

                assert response["message"]["text"] == message

            except SlackApiError as e:
                print(f"Error al enviar la notificacion de Slack: {e.response['error']}")
            except ObjectDoesNotExist as e:
                print(f"Error al obtener el usuario: {e}")
    else:
        user = instance.assigned_to

        if user:
            try:
                profile = user.profile
                slack_user_id = profile.slack_user_id

                client = WebClient(token=settings.SLACK_API_TOKEN)

                message = f"La tarea asignada a <@{user.username}> se ha actualizado: {instance.subject}"

                response = client.chat_postMessage(
                    channel=slack_user_id,
                    text=message
                )

                assert response["message"]["text"] == message

            except SlackApiError as e:
                print(f"Error al enviar la notificacion de Slack: {e.response['error']}")
            except ObjectDoesNotExist as e:
                print(f"Error al obtener el usuario: {e}")
