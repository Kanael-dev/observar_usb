import pygetwindow as gw
import pygame
import time
import threading

# ID de hardware do dispositivo USB desejado | No caso é o ID do do dispositivo que voce deseja validar se foi conectado
device_hardware_id = "USB\\VID_04E8&PID_6860&REV_0414&MI_00"

# Som quando o dispositivo for conectado
sound_path = r"C:\Users\kka\OneDrive - Energisa\Área de Trabalho\clock-alarm-8761.mp3"

# Iniciamos a variavel como False
usb_connected = False

# Função para tocar um som quando o cabo é desconectado
def play_disconnection_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play(-1)

def stop_disconnection_sound():
    pygame.mixer.quit()
    pygame.mixer.init()
    pygame.mixer.music.stop()

def check_usb_status():
    global usb_connected

    while True:
        # Valida eternamente o cabo ser conectado
        usb_device = gw.getWindowsWithTitle(device_hardware_id)

        if usb_device and not usb_connected:
            print("Cabo USB conectado!")
            usb_connected = True
            stop_disconnection_sound()  # Parar a reprodução do som
        elif not usb_device and usb_connected:
            print("Cabo USB desconectado!")
            usb_connected = False
            play_disconnection_sound()  # Iniciar a reprodução do som

        time.sleep(1)  # Aguarde 1 segundo antes de verificar novamente

# Inicia o processo para validar a conexão
usb_thread = threading.Thread(target=check_usb_status)
usb_thread.start()

usb_thread.join()
