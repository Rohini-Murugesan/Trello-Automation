def generateReport(path,Testcase_Results):
    html = """<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Report</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <link rel="stylesheet" href="report.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.14.0/css/all.css" integrity="sha384-HzLeBuhoNPvSl5KYnjx0BT+WB0QEEqLprO+NBkkk5gbc67FTaL7XIGa2w1L0Xbgc" crossorigin="anonymous">

    <style>
        .outline{
            border-radius: 10px;
            width: 100%;
            box-shadow: 0 0 15px rgb(148, 144, 144);
        }
        .title{
            cursor: pointer;
        }
        .testcase{
            border-radius: 5px;
            text-align: center;
            padding: 4px;
            margin-left: 4px;
        }
        #td2span{
            color:whitesmoke;
            padding: 4px;
            border-radius: 12px;
        }
        #image{
            height: auto;
            width: 100%;
            cursor:pointer;
        }
    </style>

</head>
<body style="background-color: whitesmoke;"  onload="Summary()">
    <script src="report.js"></script>
    <script type="text/javascript" src="report.js"></script>
    <script type="text/javascript">
        // var mydata = JSON.stringify(data);
        var img_count = 0
        var createElmAndSetAttr = function(AllAttributes,Elmtype){
            var Elm = document.createElement(Elmtype)
            for(attr in AllAttributes){
                Elm.setAttribute(attr,AllAttributes[attr])
            }
            return Elm
        }
        
        var Summary = ()=>{
            // var Summary =  document.getElementById('Summary')
            // console.log(Summary.style.cssText)
            // Summary.style = Summary.style.cssText === "top: -20px;" ? "top:0px" : "top:-20px"
            var content = document.getElementById('content')
            var maindiv_obj = {'class':'maindiv',"id":"maindiv"}
            let maindiv = document.getElementById("maindiv")
            console.log(maindiv)
              if (maindiv !== null && maindiv !== undefined){
                maindiv.remove()
              }
            var divmain = createElmAndSetAttr(maindiv_obj,'div')
            var divrow = createElmAndSetAttr({"class":"row text-dark"},'div')
            divmain.appendChild(divrow)

            var divrow1col1 = createElmAndSetAttr({"class":"col-2 mt-4 testcase bg-light"},'div')
            var divrow1col1span1 = createElmAndSetAttr({},'span')
            divrow1col1span1.innerText = "Testcase Name"
            divrow1col1.appendChild(divrow1col1span1)

            var divrow1col2 = createElmAndSetAttr({"class":"col-9 mt-4 testcase bg-light"},'div')
            var divrow1col2span = createElmAndSetAttr({},'span')
            divrow1col2span.innerText = data.testcaseName
            divrow1col2.appendChild(divrow1col2span)

            divrow.append(divrow1col1,divrow1col2)

            var divrow2 = createElmAndSetAttr({"class":"row text-dark"},'div')
            divmain.appendChild(divrow2)

            var divrow2col1 = createElmAndSetAttr({"class":"col-2 mt-4 testcase bg-light"},'div')
            var divrow2col1span1 = createElmAndSetAttr({},'span')
            divrow2col1span1.innerText = "Testcase Description"
            divrow2col1.appendChild(divrow2col1span1)

            var divrow2col2 = createElmAndSetAttr({"class":"col-9 mt-4 testcase bg-light"},'div')
            var divrow2col2span = createElmAndSetAttr({},'span')
            divrow2col2span.innerText = data.testcaseDescription
            divrow2col2.appendChild(divrow2col2span)
            divrow2.append(divrow2col1,divrow2col2)

            var divrow3 = createElmAndSetAttr({"class":"row text-dark"},'div')
            divmain.appendChild(divrow3)

            var divrow3col1 = createElmAndSetAttr({"class":"col-2 mt-4 testcase bg-light"},'div')
            var divrow3col1span1 = createElmAndSetAttr({},'span')
            divrow3col1span1.innerText = "Result"
            divrow3col1.appendChild(divrow3col1span1)

            
            var divrow3col2 = createElmAndSetAttr({"class":"col-9 m-1 mt-4 testcase"},'div')
            let result = data.Result
            status_color =  result==="PASS" ? "green": "red"
            var divrow3col2span = createElmAndSetAttr({},'span')
            divrow3col2span.innerText = result
            divrow3col2.style = "border-radius:5px;color:white;background-color:"+status_color
            divrow3col2.appendChild(divrow3col2span)

            divrow3.append(divrow3col1,divrow3col2)
            

            divmain.style = "color:whitesmoke"
            content.appendChild(divmain)
            var steps = document.getElementById('test-steps')
            for(i=0;i<data.Steps.length;i++){
                var tr = createElmAndSetAttr({},'tr')
                console.log(data.Steps[i])
                var th = createElmAndSetAttr({"scope":"row"},'th')
                th.innerText = data.Steps[i][0]
                var td1 = createElmAndSetAttr({},'td')
                td1.innerText = data.Steps[i][1]
                var td2 = createElmAndSetAttr({},'td')
                var td2span = createElmAndSetAttr({"id":"td2span","class": data.Steps[i][2] === true ? "bg-success" : "bg-danger"},'span')
                td2span.innerText = data.Steps[i][2] === true ? "PASS" : "FAIL"
                // td2span.style = data.Steps[i][2] === true ? "color:green" : "color:red"
                td2.appendChild(td2span)
                tr.append(th,td1,td2)
                steps.appendChild(tr)
            }

            var image = document.getElementById('image')
            image.src = data.Images[img_count]
            var imagename = document.getElementById('imagename')
            imagename.innerText = (img_count+1)+". "+data.Images[img_count].replace(".png","")
            imagename.style = "color:white;font-size:14px;font-style:italic"

            }
            let prev_image = ()=>{
                console.log(img_count)
                if(img_count===0){
                    img_count = data.Images.length - 1
                }else{
                    img_count--;
                }
                var image = document.getElementById('image')
                image.src = data.Images[img_count]
                var imagename = document.getElementById('imagename')
                imagename.innerText = (img_count+1)+". "+data.Images[img_count].replace(".png","")
                imagename.style = "color:white;font-size:14px;font-style:italic"
            }

            let next_image = ()=>{
                console.log(img_count)
                if(img_count === data.Images.length - 1){
                    img_count = 0
                }else{
                    img_count++;
                }
                var image = document.getElementById('image')
                image.src = data.Images[img_count]
                var imagename = document.getElementById('imagename')
                imagename.innerText = (img_count+1)+". "+data.Images[img_count].replace(".png","")
                imagename.style = "color:white;font-size:14px;font-style:italic"
            }
            let Open = ()=>{
            window.open(document.getElementById('image').src, "_blank");
            }
    </script>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>

    <div class="container-fluid mt-5">
    <div class="row">
        <div class="col-1"></div>
        <div class="col-10 outline" style="background-color: #181b30 ;">
            <div class="row text-dark text-center" >
                <div class="col-12 bg-danger text-white font-weight-bolder p-3 rounded title" id="Summary">TEST EXECUTION SUMMARY</div>
                <!-- <div class="col-4 bg-warning p-2 rounded title" id="exec_results" onclick="exec_results()">Execution Results</div>
                <div class="col-4 bg-success p-2 rounded title" id="Images" onclick="Images()">Images</div> -->
            </div>
            <div id="content">
            </div>
            <div>                  
                  <table class="table mt-5 text-light">
                    <thead class="thead-light">
                      <tr>
                        <th scope="col">#</th>
                        <th scope="col">Step Description</th>
                        <th scope="col">Result</th>
                      </tr>
                    </thead>
                    <tbody id="test-steps">
                    </tbody>
                  </table>
            </div>
            <div class="images">
                <div class="row mb-5">
                    <div class="col-2 align-self-center">
                        <button id="prev" class="btn btn-primary btn-danger offset-5" onclick="prev_image()"><i class="fas fa-chevron-left"></i></button>
                    </div>
                    <div class="col-8 align-self-center">
                        <img id="image" class="img-fluid" onclick="Open()">
                        <span id="imagename"></span>
                    </div>
                    <div class="col-2 align-self-center">
                        <button id="next" class="btn btn-primary btn-danger offset-3"  onclick="next_image()" ><i class="fas fa-chevron-right"></i></button>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-1"></div>
    </div>     
    </div>
</body>
</html>"""
    with open(path+"\\report.html", "w") as outfile:
        outfile.write(html)

