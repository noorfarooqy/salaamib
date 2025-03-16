<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <membershipheader :title="title" />

      <div class="row">
        <div class="col-sm-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <a-table class="stripped table-hover" :columns="columns" :data-source="data">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'id'">
                      <div :class="record.class">{{ record.Amount }}</div>
                    </template>
                    <template v-else-if="column.key === 'status'">
                      <span class="badge badge-pill bg-success-light" v-if="record.Status === 'Completed'">{{
                        record.Status }}</span>
                      <span class="badge badge-pill bg-danger-light" v-else-if="record.Status === 'Cancel'">{{
                        record.Status }}</span>
                    </template>
                  </template>
                </a-table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->
  <subscribersmodel></subscribersmodel>

</template>
<script>
const columns = [
  {
    title: "#",
    dataIndex: "NUM",
    sorter: {
      compare: (a, b) => {
        a = a.NUM.toLowerCase();
        b = b.NUM.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Type",
    dataIndex: "Type",
    sorter: {
      compare: (a, b) => {
        a = a.Type.toLowerCase();
        b = b.Type.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Amount",
    dataIndex: "Amount",
    key: "id",
    sorter: {
      compare: (a, b) => {
        a = a.Amount.toLowerCase();
        b = b.Amount.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Date",
    dataIndex: "Date",
    sorter: {
      compare: (a, b) => {
        a = a.Date.toLowerCase();
        b = b.Date.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Payment Type",
    dataIndex: "PaymentType",
    sorter: {
      compare: (a, b) => {
        a = a.PaymentType.toLowerCase();
        b = b.PaymentType.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },

  {
    title: "Status",
    dataIndex: "Status",
    key: "status",
    sorter: {
      compare: (a, b) => {
        a = a.Status.toLowerCase();
        b = b.Status.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
];
const data = [
  {
    NUM: "1",
    Type: "Wallet Topup",
    Amount: "+$650",
    Date: "19 Dec 2023, 06:12 PM",
    PaymentType: "Paypal",
    class: "text-success-light",
    Status: "Completed",
  },
  {
    NUM: "2",
    Type: "Purchase",
    Amount: "+$350",
    Date: "19 Dec 2023, 06:12 PM",
    PaymentType: "Cash",
    class: "text-danger",
    Status: "Cancel",
  },
  {
    NUM: "3",
    Type: "Refund",
    Amount: "+100",
    Date: "20 Jan 2023, 06:12 PM",
    PaymentType: "Paypal",
    class: "text-success-light",
    Status: "Completed",
  },
  {
    NUM: "4",
    Type: "Wallet Topup",
    Amount: "-$650",
    Date: "20 Jun 2023, 06:12 PM",
    PaymentType: "Cash",
    class: "text-success-light",
    Status: "Completed",
  },
  {
    NUM: "5",
    Type: "Purchase",
    Amount: "+$350",
    Date: "19 Dec 2023, 06:12 PM",
    PaymentType: "Paypal",
    class: "text-danger",
    Status: "Cancel",
  },
  {
    NUM: "6",
    Type: "Refund",
    Amount: "+$100",
    Date: "15 Jan 2023, 06:12 PM",
    PaymentType: "Cash",
    class: "text-danger",
    Status: "Cancel",
  },
];
export default {
  data() {
    return {
      title: "Transactions",
      data,
      columns,
    };
  },
};
</script>
