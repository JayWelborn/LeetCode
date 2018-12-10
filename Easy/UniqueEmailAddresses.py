class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        for i in range(len(emails)):
            names = emails[i].split("@")
            names[0] = names[0].replace(".", "")
            if "+" in names[0]:
                names[0] = names[0][:names[0].index("+")]
            email = names[0] + "@" + names[1]
            emails[i] = email
        return len(set(emails))
