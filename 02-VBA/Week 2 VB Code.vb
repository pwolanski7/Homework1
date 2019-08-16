Sub StockMaster():

  Dim Ticker As String
  Dim Stock_Total As Double
  Dim Summary_Table_Row As Integer
  Stock_Total = 0
  Summary_Table_Row = 2

    For Each ws In Worksheets
        LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
        ws.Range("I1") = "Ticker"
        ws.Range("J1") = "Total Volume"
        For i = 2 To LastRow
            If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
                Ticker = ws.Cells(i, 1).Value
                Stock_Total = Stock_Total + ws.Cells(i, 7).Value
                ws.Range("I" & Summary_Table_Row).Value = Ticker
                ws.Range("J" & Summary_Table_Row).Value = Stock_Total
                Summary_Table_Row = Summary_Table_Row + 1
                Stock_Total = 0
            Else
                Stock_Total = Stock_Total + ws.Cells(i, 7).Value
            End If
        Next i
        Summary_Table_Row = 2
    Next ws

End Sub