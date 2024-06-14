from winotify import Notification, audio

notificacao_erro = Notification(app_id="Erro", title="Cadastro paralizado", msg="Os nomes dos arquivos são divergentes!")
notificacao_erro.set_audio(audio.Mail, loop=False)

notificacao_finalizado = Notification(app_id="Finalizado", title="Cadastro finalizado", msg="Finalizei os cadastros!")
notificacao_finalizado.set_audio(audio.Mail, loop=False)