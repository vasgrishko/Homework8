import view
import model


def menu():
    phone_book_main = []
    while True:
        choice = view.show_menu()
        if choice == "":
            print("До свидания!")
            break
        elif choice == "1":
            rec = model.create_rec(*view.new_rec(mode="new"))
            phone_book_main.append(rec)
        elif choice == "2":
            surname = view.surname()
            recs = model.select(phone_book_main, surname)
            view.show_recs(recs)
        elif choice == "3":
            surname = view.surname()
            recs = model.select(phone_book_main, surname)
            if recs:
                idx = phone_book_main.index(recs[0])
                rec = model.create_rec(*view.new_rec(mode="update"))
                rec = model.merge(rec, recs[0])
                phone_book_main[idx] = rec
        elif choice == "4":
            surname = view.surname()
            recs = model.select(phone_book_main, surname)
            if recs:
                idx = phone_book_main.index(recs[0])
                phone_book_main.pop(idx)
        elif choice == "5":
            filename = view.file_name()
            recs = model.import_file(filename)
            phone_book_main.extend(recs)
        elif choice == "6":
            filename = view.file_name()
            model.export_file(filename, phone_book_main)
        elif choice == "7":
            view.show_all_recs(phone_book_main)
        else:
            print("Не правильный ввод")