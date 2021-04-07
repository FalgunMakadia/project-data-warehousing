import re

class Queryparser:

    def queryParser(self, query):

        typeOfQuery = query.split(' ', 1)[0]
        typeOfQuery =  typeOfQuery.lower()

        attributes = []
        if(typeOfQuery == "select"):
                txt = query
                columnList = []
                tableName = ""
                conditionalColumn = ""
                conditionalOperator  = ""
                conditionalValue = ""
                matched = re.match('(?i)(select|SELECT)[ ](.*)[ ](from|FROM)[ ](.*)', txt)
                is_match = bool(matched)
            
                if(is_match):
                    isWherePresent = re.match('(?i)(select|SELECT)[ ](.*)[ ](from|FROM)[ ](.*)[ ](where|WHERE)[ ](.*)[ ](.*)', txt)
                    is_Where_Present = bool(isWherePresent)
                    if is_Where_Present:
                        column = re.search('(?i)(select|SELECT)[ ](.*)[ ](from|FROM)[ ](.*)[ ](where|WHERE)[ ](.*)', txt)
                        columnName = column.group(2)
                        columnList = []
                        tableName = column.group(4)
                        whereCondition = column.group(6)
                        if columnName == "*":
                                if "<=" in whereCondition:
                                    conditionalOperator = "<="
                                    conColumnList = whereCondition.split("<=", 1)
                                    conValueList = whereCondition.split("<=", 2)
                                    conditionalColumn = conColumnList[0]
                                    conditionalValue = conValueList[1]
                                    columnList = []    

                                elif ">=" in whereCondition:
                                    conditionalOperator = ">="
                                    conColumnList = whereCondition.split(">=", 1)
                                    conValueList = whereCondition.split(">=", 2)
                                    conditionalColumn = conColumnList[0]
                                    conditionalValue = conValueList[1]
                                    columnList = []
                                    
                                elif "=" in whereCondition:
                                    conditionalOperator = "="
                                    conColumnList = whereCondition.split("=", 1)
                                    conValueList = whereCondition.split("=", 2)
                                    conditionalColumn = conColumnList[0]
                                    conditionalValue = conValueList[1]
                                    columnList = []
                                
                                elif "<" in whereCondition:
                                    conditionalOperator = "<"
                                    conColumnList = whereCondition.split("<", 1)
                                    conValueList = whereCondition.split("<", 2)
                                    conditionalColumn = conColumnList[0]
                                    conditionalValue = conValueList[1]
                                    columnList = []
                                   
                                elif ">" in whereCondition:
                                    conditionalOperator = ">"
                                    conColumnList = whereCondition.split(">", 1)
                                    conValueList = whereCondition.split(">", 2)
                                    conditionalColumn = conColumnList[0]
                                    conditionalValue = conValueList[1]
                                    columnList = []
                                    
                                else:
                                    print("Error in query")
                                    return attributes, False
                        else:
                            columnList = columnName.split(",")
                          
                            if "<=" in whereCondition:
                                conditionalOperator = "<="
                                conColumnList = whereCondition.split("<=", 1)
                                conValueList = whereCondition.split("<=", 2)
                                conditionalColumn = conColumnList[0]
                                conditionalValue = conValueList[1]
                                   
                            elif ">=" in whereCondition:
                                conditionalOperator = ">="
                                conColumnList = whereCondition.split(">=", 1)
                                conValueList = whereCondition.split(">=", 2)
                                conditionalColumn = conColumnList[0]
                                conditionalValue = conValueList[1]
                              
                            elif "=" in whereCondition:
                                conditionalOperator = "="
                                conColumnList = whereCondition.split("=", 1)
                                conValueList = whereCondition.split("=", 2)
                                conditionalColumn = conColumnList[0]
                                conditionalValue = conValueList[1]
                                
        
                            elif "<" in whereCondition:
                                conditionalOperator = "<"
                                conColumnList = whereCondition.split("<", 1)
                                conValueList = whereCondition.split("<", 2)
                                conditionalColumn = conColumnList[0]
                                conditionalValue = conValueList[1]
                                
                                
                            elif ">" in whereCondition:
                                conditionalOperator = ">"
                                conColumnList = whereCondition.split(">", 1)
                                conValueList = whereCondition.split(">", 2)
                                conditionalColumn = conColumnList[0]
                                conditionalValue = conValueList[1]
                                
                            else:
                                print("error in query")
                                return attributes, False
                    else :
                        column = re.search('(?i)(select|SELECT)[ ](.*)[ ](from|FROM)[ ](.*)', txt)
                        columnName = column.group(2)
                        tableName = column.group(4)
                        if bool(re.search(r"\s" ,tableName)):
                            print(" error in query")
                            return attributes, False
                        else:
                            if columnName == "*":
                                cloumnList = []
                                conditionalColumn = ""
                                conditionalValue = ""
                            else:
                                cloumnList = columnName.split(",")
                                conditionalColumn = ""
                                conditionalValue = ""
                    attributes.append(typeOfQuery)
                    attributes.append(columnList)
                    attributes.append(tableName)
                    attributes.append(conditionalColumn)
                    attributes.append(conditionalOperator)
                    attributes.append(conditionalValue)
                    
                else : 
                    print("Type Query Again")
                    return attributes, False  
        elif(typeOfQuery == "insert"):
            txt = query
            columnList = []
            valueList = []
            tableName = ""
            match = re.match('(?i)(INSERT|insert)[ ](INTO|into)[ ](.*)(VALUES|values)[ ](.*)', txt)
            is_match = bool(match)
            if is_match:
                result = re.match('(?i)(INSERT|insert)(.*)(INTO|into)(.*)(VALUES|values)((.*))', txt)
                tableAndColumnName = result.group(4)
                if ("(" in tableAndColumnName) and (")" in tableAndColumnName):
                    tableName = tableAndColumnName.split('(')[0].strip()
                    columns = tableAndColumnName.split("(")[1].strip()
                    columnsFinal = columns.split(")")[0].strip()
                    columnName = columnsFinal
                    listOfColumn = [x.strip() for x in columnName.split(',')]
                    if '' in listOfColumn:
                        print("check syntax of query")
                        return attributes, False
                    else:
                        values = result.group(6)
                        if ("(" in values) and (")" in values):
                            valuesWithBraces = result.group(6)
                            valuesWithoutBraces = re.search('\((.*)\)', valuesWithBraces)
                            finalValues = valuesWithoutBraces.group(1)
                            listOfValue = [x.strip().strip('\"').strip("\'") for x in finalValues.split(',')]
                            if len(listOfValue) == len(listOfColumn):
                                attributes.append(typeOfQuery)
                                attributes.append(tableName)
                                attributes.append(listOfColumn)
                                attributes.append(listOfValue)
                            else:
                                print("error in query")
                                return attributes, False
                        else: 
                            print(" in else condition")
                            return attributes, False
                else:
                    values = result.group(6)
                    tableName = result.group(4)
                    if ("(" in values) and (")" in values):
                            valuesWithBraces = result.group(6)
                            valuesWithoutBraces = re.search('\((.*)\)', valuesWithBraces)
                            finalValues = valuesWithoutBraces.group(1)
                            listOfValue = [x.strip().strip('\"').strip("\'") for x in finalValues.split(',')]
                            attributes.append(typeOfQuery)
                            attributes.append(tableName)
                            attributes.append(columnList) 
                            attributes.append(listOfValue)  
                    else: 
                        print("Check query syntax")
                        return attributes, False
            else:
                print("Check query syntax")
                return attributes, False

        elif(typeOfQuery == "update"):
            columnList = []
            finalValueList = []
            tableName = ""
            conditionalColumn = ""
            conditionalValue = ""
            conditionalOperator = ""
            txt = query
            match = re.match('(?i)(UPDATE|update)[ ](.*)[ ](SET|set)[ ](.*)', txt)
            is_match = bool(match) 
            if is_match:

                match2 = re.match('(?i)(UPDATE|update)[ ](.*)[ ](SET|set)[ ](.*)[ ](WHERE|where)[ ](.*)', txt)
                is_match2 = bool(match2)
                if is_match2:
                    result = re.match('(?i)(UPDATE|update)[ ](.*)[ ](SET|set)[ ](.*)[ ](WHERE|where)[ ](.*)', txt)
                    tableName = result.group(2)
                    columnAndValue = result.group(4)
                    listOfColumnAndValue = columnAndValue.split(',')
                    columnNameList = []
                    valuesList = []
                    for listOfColumnAndValue in listOfColumnAndValue:
                        listOfValue = listOfColumnAndValue.split("=")
                        column = listOfValue[0]
                        values = listOfValue[1]
                        column = column.strip().strip("\'").strip("\"")
                        values = values.strip().strip("\'").strip("\"") 
                        columnNameList.append(column)
                        valuesList.append(values)
                    whereCondition =  result.group(6)
                    if "<=" in whereCondition:
                        conditionalOperator = "<="
                        conColumnList = whereCondition.split("<=", 1)
                        conValueList = whereCondition.split("<=", 2)
                        conditionalColumn = conColumnList[0].strip()
                        conditionalValue = conValueList[1].strip()
                            
                    elif ">=" in whereCondition:
                        conditionalOperator = ">="
                        conColumnList = whereCondition.split(">=", 1)
                        conValueList = whereCondition.split(">=", 2)
                        conditionalColumn = conColumnList[0].strip()
                        conditionalValue = conValueList[1].strip()
                        
                    elif "=" in whereCondition:
                        conditionalOperator = "="
                        conColumnList = whereCondition.split("=", 1)
                        conValueList = whereCondition.split("=", 2)
                        conditionalColumn = conColumnList[0].strip()
                        conditionalValue = conValueList[1].strip()
                    
                    elif "<" in whereCondition:
                        conditionalOperator = "<"
                        conColumnList = whereCondition.split("<", 1)
                        conValueList = whereCondition.split("<", 2)
                        conditionalColumn = conColumnList[0].strip()
                        conditionalValue = conValueList[1].strip()
                    
                    elif ">" in whereCondition:
                        conditionalOperator = ">"
                        conColumnList = whereCondition.split(">", 1)
                        conValueList = whereCondition.split(">", 2)
                        conditionalColumn = conColumnList[0].strip()
                        conditionalValue = conValueList[1].strip()
                    
                    columnList = columnNameList
                    finalValueList = valuesList  
                    attributes.append(typeOfQuery)
                    attributes.append(columnList)
                    attributes.append(tableName)
                    attributes.append(finalValueList)
                    attributes.append(conditionalColumn)
                    attributes.append(conditionalOperator)
                    attributes.append(conditionalValue)
                else:
                    result = re.match('(?i)(UPDATE|update)[ ](.*)[ ](SET|set)[ ](.*)', txt)
                    tableName = result.group(2)
                    columnAndValue = result.group(4)
                    listOfColumnAndValue = columnAndValue.split(',')
                    columnNameList = []
                    valuesList = []
                    conditionalColumn = ""
                    conditionalValue = ""
                    conditionalOperator = ""

                    for listOfColumnAndValue in listOfColumnAndValue:
                        listOfValue = listOfColumnAndValue.split("=")
                        column = listOfValue[0]
                        values = listOfValue[1]
                        column = column.strip().strip("\'").strip("\"")
                        values = values.strip().strip("\'").strip("\"") 
                        columnNameList.append(column)
                        valuesList.append(values)
                    columnList = columnNameList
                    finalValueList = valuesList  
                    attributes.append(typeOfQuery)
                    attributes.append(columnList)
                    attributes.append(tableName)
                    attributes.append(finalValueList)
                    attributes.append(conditionalColumn)
                    attributes.append(conditionalOperator)
                    attributes.append(conditionalValue)
            else:
                print("Check query syntax")
                return attributes, False
                
        elif(typeOfQuery == "delete"):
            txt = query
            tableName = ""
            conditionalColumn = ""
            conditionalValue = ""
            conditionalOperator = ""
            match = re.match('(?i)(DELETE|delete)[ ](FROM|from)[ ](.*)[ ](WHERE|where)[ ](.*)', txt)
            is_match = bool(match) 
            if is_match:
                result = re.match('(?i)(DELETE|delete)[ ](FROM|from)[ ](.*)[ ](WHERE|where)[ ](.*)', txt)
                tableName = result.group(3)
                whereCondition =  result.group(5)
                if "<=" in whereCondition:
                    conditionalOperator = "<="
                    conColumnList = whereCondition.split("<=", 1)
                    conValueList = whereCondition.split("<=", 2)
                    conditionalColumn = conColumnList[0]
                    conditionalValue = conValueList[1]
                        
                elif ">=" in whereCondition:
                    conditionalOperator = ">="
                    conColumnList = whereCondition.split(">=", 1)
                    conValueList = whereCondition.split(">=", 2)
                    conditionalColumn = conColumnList[0]
                    conditionalValue = conValueList[1]
                    
                elif "=" in whereCondition:
                    conditionalOperator = "="
                    conColumnList = whereCondition.split("=", 1)
                    conValueList = whereCondition.split("=", 2)
                    conditionalColumn = conColumnList[0]
                    conditionalValue = conValueList[1]
                
                elif "<" in whereCondition:
                    conditionalOperator = "<"
                    conColumnList = whereCondition.split("<", 1)
                    conValueList = whereCondition.split("<", 2)
                    conditionalColumn = conColumnList[0]
                    conditionalValue = conValueList[1]
                   
                elif ">" in whereCondition:
                    conditionalOperator = ">"
                    conColumnList = whereCondition.split(">", 1)
                    conValueList = whereCondition.split(">", 2)
                    conditionalColumn = conColumnList[0]
                    conditionalValue = conValueList[1]  
                attributes.append(typeOfQuery)
                attributes.append(tableName)
                attributes.append(conditionalColumn)
                attributes.append(conditionalOperator)
                attributes.append(conditionalValue)              
            else:
                print("Check query syntax")
                return attributes, False

        elif(typeOfQuery == "create"):
            txt = query
            tableName = ""
            columnList = ""
            valueList = ""
            match = re.match('(?i)(CREATE|create)[ ](TABLE|table)[ ](.*)[ ](.*)', txt)
            is_match = bool(match)
            if is_match:
                result = re.match('(?i)(CREATE\\sTABLE\\s(\\w+)\\s?\\(((?:\\s?\\w+\\s\\w+\\(?[0-9]*\\)?,?)+)\\)\\s?;)', txt)
                tableName = result.group(2)
                columns = result.group(3)
                columnString = columns.split("\\s*,\\s*")
                columnName  = []
                dataType  = []
                columnslist = columns.split(",")
                lengthOfColummnList = 0
                for s in columnslist:
                    cloumnAfterRemovingSpace = s.split()
                    firstElementOfList =  cloumnAfterRemovingSpace[0]
                    lastElementOfList = cloumnAfterRemovingSpace[1]
                    columnName.append(firstElementOfList)
                    dataType.append(lastElementOfList)
                    lengthOfColummnList = lengthOfColummnList +1

                attributes.append(typeOfQuery)
                attributes.append(lengthOfColummnList)
                attributes.append(columnName)
                attributes.append(dataType)
                attributes.append(tableName)
                
            else:
                print("Check syntax of query")
                return attributes, False
        else:
            print("Check syntax of query")
            return attributes, False

        return  attributes , True