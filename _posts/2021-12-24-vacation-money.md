---
date: 2021-12-24 12:00:00 +0200
title: "How to split money fairly after a vacation"
layout: post
categories: Math
---

After a week of fun and relax with friends, splurging money without second
thoughts, it is time to make sums and make sure everybody paid what is fair.
How to do this?

<!-- more -->

First, everybody should sum up all money they spent for the group, excluding
personal expenses. Assume there are four people: Alice spent 887 euros, Bob
spent 736, Charlie 609 and David 48. The fairest way of splitting money is
making sure that after the transfers have been made everybody spent the exactly
average, in this case 570 euros.

|         | Spent | Gives to others in total | Spent after transfers |
|---------+-------+--------------------------+-----------------------|
| Alice   |   887 |                     -317 | 887-317=570           |
| Bob     |   736 |                     -166 | 736-166=570           |
| Charlie |   609 |                      -39 | 609-39=570            |
| David   |    48 |                      522 | 48+522=570            |

This means that Alice should receive 317 euros from the other three, Bob 166,
Charlie 38 and David, who did not spend much during the vacation, should give
522 euros in total. By summing the money spent and the money received from the
others, everybody will have spent exactly the average of 570 euros.

But how much of the 522 euros that David gives should go to Alice, how much to
Bob, and how much to Charlie? And, even though in aggregate Bob should receive
166 euros from the others, he should certainly give some to Alice who spent more
than him during the vacation. How to deal with this?

Consider Alice, who spent 887 euros for the group of four friends; dividing
fairly, Alice spent 887/4=221.75 euros for each member, including herself. This
means that everybody else should give Alice 221.75 euros to repay for her
expenses. Similarly, Bob spent 736/4=184 euros for each member, which means that
he should receive that amount from the others. Now, since Bob owes Alice 221.75
euros and Alice owes Bob 184 euros, they can settle this by having Bob give
Alice 221.75-184=37.75 euros. If we put into a table how much each person should
receive from the others, we have:

|         | Spent | Receives from each friend |
|---------+-------+---------------------------|
| Alice   |   887 | 887/4=221.75              |
| Bob     |   736 | 736/4=184                 |
| Charlie |   609 | 609/4=152.25              |
| David   |    48 | 48/4=12                   |

We can now find exactly how much everybody should give to each other friend by
taking the difference of the quantities above, as we did for Alice and Bob. If
we do this, we get the following table, with positive amounts denoting money
given and negatives denoting money received:


| &#8595; gives to &#8594; |  Alice |    Bob | Charlie |   David | Total Given |
|--------------------------+--------+--------+---------+---------+-------------|
| Alice                    |      0 | -37.75 |  -69.50 | -209.75 |        -317 |
| Bob                      |  37.75 |      0 |  -31.75 |    -172 |        -166 |
| Charlie                  |  69.50 |  31.75 |       0 |  140.25 |         -39 |
| David                    | 209.75 |    172 |  140.25 |       0 |         522 |
|--------------------------+--------+--------+---------+---------+-------------|
| Total Received           |    317 |    166 |      39 |    -522 |             |


Summing the numbers in each row results in the numbers we saw at the beginning,
i.e. how much each person should give to or receive from each other. In
addition, we know how much each person owes to each other person by looking at
the relevant cell in the table.

The math is simple, but here's a widget to do this easily for your own vacation
with up to six friends.


<style>
.row{ display:flex;flex-wrap:wrap; margin-bottom: 15px;}
.col-left{flex:0 0 auto;width:20%}
.col-right{flex:0 0 auto;width:80%}
.container{width:100%;margin-right:auto;margin-left:auto;border:1px solid gray;border-radius:10px;padding:30px;margin-top:50px;}
.topspace{margin-top:50px;}
table th, table td {border:0px; background-color: white;}
table{text-align: right; border:0px;}
</style>

<div class="container">
  <div>
    <h4>Total spending by each friend:</h4>
  </div>

  <div class="row">
    <div class="col-left"><label for="spending-1" class="col-form-label">Friend A</label></div>
    <div class="col-right"><input type="text" id="spending-1" class="form-control" value="887.00"></div>
  </div>
  <div class="row">
    <div class="col-left"><label for="spending-2" class="col-form-label">Friend B</label></div>
    <div class="col-right"><input type="text" id="spending-2" class="form-control" value="736.00"></div>
  </div>
  <div class="row">
    <div class="col-left"><label for="spending-3" class="col-form-label">Friend C</label></div>
    <div class="col-right"><input type="text" id="spending-3" class="form-control" value="609.00"></div>
  </div>
  <div class="row">
    <div class="col-left"><label for="spending-4" class="col-form-label">Friend D</label></div>
    <div class="col-right"><input type="text" id="spending-4" class="form-control" value="48.00"></div>
  </div>
  <div class="row">
    <div class="col-left"><label for="spending-5" class="col-form-label">Friend E</label></div>
    <div class="col-right"><input type="text" id="spending-5" class="form-control" value=""></div>
  </div>
  <div class="row">
    <div class="col-left"><label for="spending-6" class="col-form-label">Friend F</label></div>
    <div class="col-right"><input type="text" id="spending-6" class="form-control" value=""></div>
  </div>
  <div class="row">
    <button class="btn btn-primary" onclick="calculate()">Calculate!</button>
  </div>
  <div class="topspace">
    <h4>Money transfers:</h4>
  </div>

  <table style="margin-bottom:0px;">
    <thead>
      <tr>
        <th scope="col"> &#8595; to &#8594; </th>
        <th scope="col">Friend A</th>
        <th scope="col">Friend B</th>
        <th scope="col">Friend C</th>
        <th scope="col">Friend D</th>
        <th scope="col">Friend E</th>
        <th scope="col">Friend F</th>
        <th scope="col">Gives</th>
      </tr>
    </thead>
    <tbody>
      <tr><th scope="row">Friend A</th><td id="g11"></td><td id="g12"></td><td id="g13"></td><td id="g14"></td><td id="g15"></td><td id="g16"></td><th scope="row" id="g1"></th></tr>
      <tr><th scope="row">Friend B</th><td id="g21"></td><td id="g22"></td><td id="g23"></td><td id="g24"></td><td id="g25"></td><td id="g26"></td><th scope="row" id="g2"></th></tr>
      <tr><th scope="row">Friend C</th><td id="g31"></td><td id="g32"></td><td id="g33"></td><td id="g34"></td><td id="g35"></td><td id="g36"></td><th scope="row" id="g3"></th></tr>
      <tr><th scope="row">Friend D</th><td id="g41"></td><td id="g42"></td><td id="g43"></td><td id="g44"></td><td id="g45"></td><td id="g46"></td><th scope="row" id="g4"></th></tr>
      <tr><th scope="row">Friend E</th><td id="g51"></td><td id="g52"></td><td id="g53"></td><td id="g54"></td><td id="g55"></td><td id="g56"></td><th scope="row" id="g5"></th></tr>
      <tr><th scope="row">Friend F</th><td id="g61"></td><td id="g62"></td><td id="g63"></td><td id="g64"></td><td id="g65"></td><td id="g66"></td><th scope="row" id="g6"></th></tr>
    </tbody>
    <tfoot>
      <tr>
        <th scope="col">Receives</th>
        <th scope="col" id="r1"></th>
        <th scope="col" id="r2"></th>
        <th scope="col" id="r3"></th>
        <th scope="col" id="r4"></th>
        <th scope="col" id="r5"></th>
        <th scope="col" id="r6"></th>
        <th scope="col" id="r7"></th>
      </tr>
    </tfoot>
  </table>
</div>


<script type="text/javascript">
var maxF = 6;

function readSpendings() {
  var spendings = [];
  var alerts = 0;

  // read each person's spending
  for(var i = 1; i <= maxF; i++) {
    // make all calculations using integers representing euro cents
    // negative values represent missing friends

    var txt = document.getElementById("spending-" + i).value;
    if(txt == "") {
      spent = -1;
    }
    else {
      var spent = Math.floor(100 * Number(txt));
      if(spent < 0 || isNaN(spent)) {
        if (alerts == 0) {
          alert("Negative and invalid numbers will be ignored.");
        }
        spent = -1;
        alerts += 1;
      }
    }

    spendings.push(spent);
  }

  return spendings;
}

function computeAndWritePairwise(spendings) {
  // compute owned to each person
  var nof = 0;
  for(var i = 0; i < maxF; i++) {
    if(spendings[i] >= 0) {
      nof += 1;
    }
  }

  var owed = [];
  for(var i = 0; i < maxF; i++) {
    owed[i] = spendings[i] / nof;
  }

  // compute pairwise money transfers and write to table
  var gives = [];
  for(var i = 0; i < maxF; i++) {
    var tot_gives = 0.0;
    for(var j = 0; j < maxF; j++) {
      var idd = "g" + (i + 1) + (j + 1);
      if(spendings[i] >= 0 && spendings[j] >= 0) {
        var transfer = (owed[j] - owed[i]);
        tot_gives += transfer;
        if(transfer > 0) {
          document.getElementById(idd).innerText = "" + (transfer / 100).toFixed(2);
        }
      }
      else {
        document.getElementById(idd).innerText = "";
      }
    }
    gives.push(tot_gives);
  }

  return gives;
}


function writeMarginals(spendings, gives) {
  // write marginals
  for(var i = 0; i < maxF; i++) {
    if(spendings[i] >= 0) {
      var g = 0;
      var r = 0;

      if(gives[i] >= 0) {
        g = gives[i] / 100;
        r = 0;
      }
      else if(gives[i] <= 0) {
         g = 0;
         r = -gives[i] / 100;
      }

      document.getElementById("g" + (i + 1)).innerText = "" + g.toFixed(2);
      document.getElementById("r" + (i + 1)).innerText = "" + r.toFixed(2);
    }
    else {
      document.getElementById("g" + (i + 1)).innerText = "";
      document.getElementById("r" + (i + 1)).innerText = "";
    }
  }
}

function calculate() {
  spendings = readSpendings()
  gives = computeAndWritePairwise(spendings);
  writeMarginals(spendings, gives);
}

</script>
