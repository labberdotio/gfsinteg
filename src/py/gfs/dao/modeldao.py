

# 
class GFSModelDAO(object):

    # 
    def makeModel(self, label, properties = {}):
        pass

    def model(self, resource, properties = {}):
        return self.makeModel(
            label = resource, 
            properties = properties
        )        

    def saveModel(self, model, label, id = None):
        pass

    # def create(self, namespace):
    # def create(self, dao):
    def createModel(self, model):
        pass

    def createModels(self, models):
        pass

    def getModel(self, label, id):
        pass

    def getModels(self, label, ids = []):
        pass

    def queryModel(self, label = None, matching = {}):
        pass

    def queryModels(self, label = None, matching = {}):
        pass

    def updateModel(self, model, **kwargs):
        pass

    def updateModels(self, models):
        pass

    # Convenience method to encapsulate the update logic
    # def createOrUpdate(self, namespace, **kwargs):
    def createOrUpdateModel(self, model, **kwargs):
        pass

    # Convenience method to encapsulate the update logic
    # def createOrUpdate(self, namespace, **kwargs):
    def createOrUpdateModels(self, models, **kwargs):
        pass

    def deleteModel(self, model):
        pass

    def deleteModels(self, models):
        pass
