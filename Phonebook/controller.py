
import operations as o
import user_interface as ui
import time
import log

def book():
    ui.hello()
    while True:        
        command=ui.phone_menu()
        if command==1:            
            o.print_phone_book(o.t)
            log.log('Просмотр списка контактов','успешно')
            time.sleep(2)              
        elif command == 2:
            cont=ui.search()
            contact=o.search_contact(cont)
            time.sleep(2)
            c=ui.search_submenu()
            if c==1:
                log.log('Удаление контакта',f'{contact}')
                o.del_phone_number(contact)
            else:                
                new_contact=ui.input_new_contact()
                o.replace_phone_contact(contact,new_contact)
                log.log(f'Контакт {contact}',f'Изменен на {new_contact}')
        elif command == 3:
            contact=ui.input_new_contact()
            o.save_phone_number(contact)
            log.log(f'Добавлен контакт',f'{contact}') 
        elif command == 4:
            c=ui.recording_database()
            if c==1:
                o.export(o.c,o.t)
                log.log('Экспорт БД из contacts.txt','В файл contacts.csv ') 
        elif command == 5:
            c=ui.recording_database()
            if c==1:
                o.export(o.t,o.c)
                log.log('Экспорт БД из contacts.csv','В файл contacts.txt ') 
        else:
            ui.by()
            break

    