<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <profitlosslist-header :title="title" />
      <!-- /Page Header -->

      <div class="profit-menu">
        <div class="row">
          <div class="col-lg-2 col-md-6 col-sm-12">
            <div class="input-block mb-3">
              <label>Period</label>
              <ul class="form-group">
                <li>
                  <vue-select :options="Profityear" placeholder="This Year" />
                </li>
              </ul>
            </div>
          </div>
          <div class="col-lg-2 col-md-6 col-sm-12">
            <div class="input-block mb-3">
              <label>From</label>
              <div class="cal-icon cal-icon-info">
                <date-picker v-model="startdate" type="text" class="datetimepicker form-control" placeholder="01 Jan 2023"
                  :editable="true" :clearable="false" :input-format="dateFormat" />
                <i class="feather feather-calendar calendar-icon"></i>
              </div>
            </div>
          </div>
          <div class="col-lg-2 col-md-6 col-sm-12">
            <div class="input-block mb-3">
              <label>To</label>
              <div class="cal-icon cal-icon-info">
                <date-picker v-model="startdate1" type="text" class="datetimepicker form-control" placeholder="31 Mar 2023"
                  :editable="true" :clearable="false" :input-format="dateFormat" />
                <i class="feather feather-calendar calendar-icon"></i>
              </div>
            </div>
          </div>
          <div class="col-lg-2 col-md-6 col-sm-12">
            <div class="input-block mb-3">
              <label>Display Columns by</label>
              <ul class="form-group">
                <li>
                  <vue-select :options="Profitmonth" placeholder="Month" />
                </li>
              </ul>
            </div>
          </div>
          <div class="col-lg-2 col-md-6 col-sm-12">
            <div class="input-block mb-3">
              <label>Accounting Method</label>
              <ul class="form-group">
                <li>
                  <vue-select :options="Profitaccrual" placeholder="Accrual" />
                </li>
              </ul>
            </div>
          </div>
          <div class="col-lg-2 col-md-6 col-sm-12">
            <a class="btn btn-primary loss" href="javascript:;"> Run</a>
          </div>
        </div>
      </div>

      <!-- Search Filter -->
      <div id="filter_inputs" class="card filter-card">
        <div class="card-body pb-0">
          <div class="row">
            <div class="col-sm-6 col-md-3">
              <div class="input-block mb-3">
                <label>Name</label>
                <input type="text" class="form-control" />
              </div>
            </div>
            <div class="col-sm-6 col-md-3">
              <div class="input-block mb-3">
                <label>Email</label>
                <input type="text" class="form-control" />
              </div>
            </div>
            <div class="col-sm-6 col-md-3">
              <div class="input-block mb-3">
                <label>Phone</label>
                <input type="text" class="form-control" />
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- /Search Filter -->

      <div class="row">
        <div class="col-sm-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <div class="table-profit-loss">
                  <table class="table table-center">
                    <thead class="thead-light loss">
                      <tr>
                        <th>Info</th>
                        <th>Jan 2023</th>
                        <th>Feb 2023</th>
                        <th>Mar 2023</th>
                        <th>Total</th>
                      </tr>
                    </thead>
                    <tr>
                      <td class="profit space" colspan="5">
                        <table class="table table-center profit">
                          <thead class="profitloss-heading">
                            <tr>
                              <th class="table-profit-head" colspan="5">Income</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr class="proft-head">
                              <td>Stripe Sales</td>
                              <td>$3,06,386.00</td>
                              <td>$2,61,738.00</td>
                              <td>$2,82,463.00</td>
                              <td>$8,50,587.00</td>
                            </tr>
                          </tbody>
                          <tr class="profitloss-bg">
                            <td>
                              <h6>Total Income</h6>
                            </td>
                            <td>
                              <h6>$3,06,386.00</h6>
                            </td>
                            <td>
                              <h6>$2,61,738.00</h6>
                            </td>
                            <td>
                              <h6>$2,82,463.00</h6>
                            </td>
                            <td>
                              <h6>$8,50,587.00</h6>
                            </td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                    <tr>
                      <td class="loss-space" colspan="5">
                        <table class="table table-center profit">
                          <thead class="profitloss-heading">
                            <tr>
                              <th class="table-profit-head" colspan="5">Expenses</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td>Exchange Gain or Losses</td>
                              <td>$0.00</td>
                              <td>$0.00</td>
                              <td>$0.00</td>
                              <td>$0.00</td>
                            </tr>
                            <tr class="proft-head">
                              <td>Stripe Fees</td>
                              <td>$2,81,687.00</td>
                              <td>$3,73,518.00</td>
                              <td>$2,17,936.00</td>
                              <td>$8,73,141.00</td>
                            </tr>
                          </tbody>

                          <tr class="profitloss-bg">
                            <td>
                              <h6>Total Expense</h6>
                            </td>
                            <td>
                              <h6>$2,58,136.00</h6>
                            </td>
                            <td>
                              <h6>$1,38,471.00</h6>
                            </td>
                            <td>
                              <h6>$2,61,682.00</h6>
                            </td>
                            <td>
                              <h6>$6,58,289.00</h6>
                            </td>
                          </tr>
                          <tr class="profitloss-bg">
                            <td>
                              <h6>Net Income</h6>
                            </td>
                            <td>
                              <h6>$2,69,276.00</h6>
                            </td>
                            <td>
                              <h6>$2,75,638.00</h6>
                            </td>
                            <td>
                              <h6>$2,51,629.00</h6>
                            </td>
                            <td>
                              <h6>$7,96,543.00</h6>
                            </td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <profitmodel></profitmodel>
</template>
<script>
import { ref } from "vue";
const currentDate = ref(new Date());
const currentDate1 = ref(new Date());
export default {
  data() {
    return {
      title: "Profit & Loss",
      startdate: currentDate,
      startdate1: currentDate1,
      dateFormat: "dd-MM-yyyy",
      Profitaccrual: ["Accrual"],
      Profitmonth: [
        "Month",
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
      ],
      Profityear: ["This Year", "2022", "2021", "2020"],
    };
  },
};
</script>
