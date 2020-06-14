from read_csv_file import *
from ansible_package.AnsibleTemplates import *

if __name__ == '__main__':

    file = CsvFile("saas.csv")
    ansibleinventrory = AnsibleTemplates("ansible_inventory_template")
    sshconfig_template = AnsibleTemplates("config")

    for row in file.opencsvfile().items():
        line_count = 0
        ansibleinventoryfile = ansibleinventrory.rendertemplatefile(ambiente=row[0], gateway_ip=row[1]['gateway'],
                                                                    oracle=row[1]['oracle'], tomcat=row[1]['tomcat'])
        sshconfig = sshconfig_template.rendertemplatefile(ambiente=row[0], gateway_ip=row[1]['gateway'],
                                                                    oracle=row[1]['oracle'], tomcat=row[1]['tomcat'])

        ansibleinventrory.createansiblefile(ansibleinventoryfile, "ansible_inventory_%s" % row[0])
        sshconfig_template.createansiblefile(sshconfig,"config_%s" % row[0])

