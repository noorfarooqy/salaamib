<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <taxpurchase-header :title="title" />
      <!-- /Page Header -->

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
                <a-table class="stripped table-hover" :columns="columns" :data-source="data">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'Customer'">
                      <td>
                        <h2 class="table-avatar d-flex">
                          <router-link to="/profile" class="avatar avatar-md me-2 companies">
                            <img class="avatar-img rounded-circle" :src="require(`@/assets/img/profiles/${record.Image}`)"
                              alt="User Image" /></router-link>
                          <router-link to="/profile">Johny Charles</router-link>
                        </h2>
                      </td>
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
  <taxpurchasemodel></taxpurchasemodel>
</template>
<script>
const columns = [
  {
    title: "#",
    dataIndex: "id",
    key: "id",
    sorter: {
      compare: (a, b) => {
        a = a.id.toLowerCase();
        b = b.id.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Customer",
    dataIndex: "Customer",
    key: "Customer",
    sorter: {
      compare: (a, b) => {
        a = a.Customer.toLowerCase();
        b = b.Customer.toLowerCase();
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
    title: "Invoice No",
    dataIndex: "InvoiceNo",
    sorter: {
      compare: (a, b) => {
        a = a.InvoiceNo.toLowerCase();
        b = b.InvoiceNo.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Total Amount",
    dataIndex: "TotalAmount",
    sorter: {
      compare: (a, b) => {
        a = a.TotalAmount.toLowerCase();
        b = b.TotalAmount.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Payment Method",
    dataIndex: "PaymentMethod",
    sorter: {
      compare: (a, b) => {
        a = a.PaymentMethod.toLowerCase();
        b = b.PaymentMethod.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Discount",
    dataIndex: "Discount",
    sorter: {
      compare: (a, b) => {
        a = a.Discount.toLowerCase();
        b = b.Discount.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Tax Amount",
    dataIndex: "TaxAmount",
    sorter: {
      compare: (a, b) => {
        a = a.TaxAmount.toLowerCase();
        b = b.TaxAmount.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  }
];
const data = [
  {
    id: "1",
    Image: "avatar-14.jpg",
    Customer: "John Smith",
    Date: "01 Aug 2023",
    InvoiceNo: "INV312345",
    TotalAmount: "$28000.00",
    PaymentMethod: "Cash",
    Discount: "10",
    TaxAmount: "$280",
  },
  {
    id: "2",
    Image: "avatar-15.jpg",
    Customer: "Johny Charles",
    Date: "13 Aug 2023",
    InvoiceNo: "INV472894",
    TotalAmount: "$32000.00",
    PaymentMethod: "Cash",
    Discount: "7",
    TaxAmount: "$340",
  },
  {
    id: "3",
    Image: "avatar-16.jpg",
    Customer: "Robert George",
    Date: "16 Sep 2023",
    InvoiceNo: "INV562967",
    TotalAmount: "$10000.00",
    PaymentMethod: "Cash",
    Discount: "12",
    TaxAmount: "$170",
  },
  {
    id: "4",
    Image: "avatar-17.jpg",
    Customer: "Sharonda Letha",
    Date: "24 Sep 2023",
    InvoiceNo: "INV012649",
    TotalAmount: "$12000.00",
    PaymentMethod: "Cash",
    Discount: "18",
    TaxAmount: "$520",
  },
  {
    id: "5",
    Image: "avatar-18.jpg",
    Customer: "Pricillia Maureen",
    Date: "10 Oct 2023",
    InvoiceNo: "INV941759",
    TotalAmount: "$16000.00",
    PaymentMethod: "Cash",
    Discount: "5",
    TaxAmount: "$270",
  },
  {
    id: "6",
    Image: "avatar-19.jpg",
    Customer: "Randall Hollis",
    Date: "29 Oct 2023",
    InvoiceNo: "INV375016",
    TotalAmount: "$22000.00",
    PaymentMethod: "Cash",
    Discount: "16",
    TaxAmount: "$350",
  },
];
export default {
  data() {
    return {
      title: "Tax Report",
      data,
      columns,
    };
  },
};
</script>
