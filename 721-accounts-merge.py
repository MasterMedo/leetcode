from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        mail_id = {}
        id_mail = defaultdict(list)
        id_name = {}
        for i, (name, *mails) in enumerate(accounts):
            mails = set(mails)
            id_name[i] = name
            id_mail[i] = mails
            same_ids = {mail_id[mail] for mail in mails if mail in mail_id}
            for j in same_ids:
                if id_name[j] == name:
                    for mail in id_mail[j]:
                        mails.add(mail)
                    del id_mail[j]
                    del id_name[j]

            for mail in mails:
                mail_id[mail] = i

        return [[id_name[i], *sorted(id_mail[i])] for i in id_mail]
