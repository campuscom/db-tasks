"""
Remove tagged careers which no longer exists from course and certificate
"""
from client import MongoEngine
from services import mongo_data_service


def main():
    MongoEngine.connect()

    print('####### Certificate #######')
    certificates = mongo_data_service.get_all_certificate_with_careers()
    for cert in certificates:
        old_list = []
        new_list = []
        print("Certificate: "+cert.id)
        for career in cert.careers:
            print("Career: "+career.id)
            old_list.append(career)
            if hasattr(career, 'name'):
                print(career.name)
                new_list.append(career)
            else:
                print('career missing')

        cert.update(
            pull_all__careers=old_list
        )
        cert.update(
            add_to_set__careers=new_list
        )


if __name__ == '__main__':
    main()
