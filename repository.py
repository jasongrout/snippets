class Repository(object):
    def __init__(self, path):
        self.path=path

    def new_revision(self, message, files):
        """
        files is a dictionary of the form {'filename': content, 'filename': content}.  Not all of the files in the repository need to be listed.  Any files that are listed are set to the value of content and the changes are committed with the commit message.
        """
        for filename, content in files:
            # be careful about not opening filenames that are above self.path in the directory tree!
            with open(os.path.join(self.path, filename),'w') as f:
                f.write(content)
            # need a way of deleting files too
        self.commit(message)

    def commit(self, message):
        "Commit the current revision to the repository."

    def file(self, filename, revision='tip'):
        "Return the contents of filename at the revision specified."
        pass
        
    def list_files(self, revision='tip'):
        "Return the list of filenames at the specified revision."
        pass

    def create(self, path):
        "Create an empty repository"
        pass

    def ancestors(self, revision='tip'):
        "Return a list of revision ids of ancestors to the specified revision"
        pass

from mercurial import commands, ui, hg, revset

class HGRepository(Repository):
    def __init__(self, path):
        super(HGRepository, self).__init__(path)
        self.ui = ui.ui()
        self.repo = hg.repository(self.ui, self.path)
        
        
    def commit(self, message):
        commands.commit(self.ui, self.repo, message=message, addremove=True)

    def file(self, filename, revision='tip'):
        "Return the contents of filename at the revision specified."
        return self.repo[revision][filename].data()
        
    def list_files(self, revision='tip'):
        "Return the list of filenames at the specified revision."
        from mercurial.cmdutils import matchall
        return list(self.repo[revision].walk(matchall(self.repo)))

    def create(self, path):
        "Create an empty repository"
        commands.init(self.ui, path)

    def ancestors(self, revision='tip'):
        "Return a list of revision ids of ancestors to the specified revision"
        return [str(c) for c in self.repo[revision].ancestors()]

