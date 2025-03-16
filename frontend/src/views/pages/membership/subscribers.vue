<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <membershipheader :title="title" />

      <!-- Table -->
      <div class="row">
        <div class="col-sm-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <a-table class="stripped table-hover" :columns="columns" :data-source="data">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'id'">
                      <h2 class="table-avatar d-flex">
                        <router-link to="/profile" class="avatar avatar-sm me-2"><img class="avatar-img rounded-circle"
                            :src="require(`@/assets/img/profiles/${record.img}`)" alt="User Image" /></router-link>
                        <router-link to="/profile">{{ record.ProviderName }}
                          <span>{{ record.mail }}</span></router-link>
                      </h2>
                    </template>
                  </template>
                </a-table>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- /Table -->
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
    title: "Provider Name",
    dataIndex: "ProviderName",
    key: "id",
    sorter: {
      compare: (a, b) => {
        a = a.ProviderName.toLowerCase();
        b = b.ProviderName.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Subscription",
    dataIndex: "Subscription",
    sorter: {
      compare: (a, b) => {
        a = a.Subscription.toLowerCase();
        b = b.Subscription.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Amount",
    dataIndex: "Amount",
    sorter: {
      compare: (a, b) => {
        a = a.Amount.toLowerCase();
        b = b.Amount.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Subscription Durations",
    dataIndex: "SubscriptionDurations",
    sorter: {
      compare: (a, b) => {
        a = a.SubscriptionDurations.toLowerCase();
        b = b.SubscriptionDurations.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Start Date",
    dataIndex: "StartDate",
    sorter: {
      compare: (a, b) => {
        a = a.StartDate.toLowerCase();
        b = b.StartDate.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "End Date",
    dataIndex: "EndDate",
    sorter: {
      compare: (a, b) => {
        a = a.EndDate.toLowerCase();
        b = b.EndDate.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
];
const data = [
  {
    NUM: "1",
    img: "avatar-14.jpg",
    ProviderName: "John Smith",
    mail: "john@example.com",
    Subscription: "Enterprise",
    Amount: "$650",
    SubscriptionDurations: "One Year",
    StartDate: "19 Dec 2023, 06:12 PM",
    EndDate: "19 Dec 2023, 06:12 PM",
  },
  {
    NUM: "2",
    img: "avatar-15.jpg",
    ProviderName: "Johnny",
    mail: "johnny@example.com",
    Subscription: "Standard",
    Amount: "$350",
    SubscriptionDurations: "6 Month",
    StartDate: "15 Dec 2023, 04:35 PM",
    EndDate: "15 April 2023, 04:35 PM",
  },
  {
    NUM: "3",
    img: "avatar-16.jpg",
    ProviderName: "Robert",
    mail: "robert@example.com",
    Subscription: "Basic",
    Amount: "$850",
    SubscriptionDurations: "1 Month",
    StartDate: "04 Dec 2023, 04:35 PM",
    EndDate: "05 April 2023, 04:35 PM",
  },
  {
    NUM: "4",
    img: "avatar-17.jpg",
    ProviderName: "Sharonda",
    mail: "sharon@example.com",
    Subscription: "Enterprise",
    Amount: "$950",
    SubscriptionDurations: "One Year",
    StartDate: "12 Dec 2023, 04:35 PM",
    EndDate: "13 April 2023, 04:35 PM",
  },
  {
    NUM: "5",
    img: "avatar-18.jpg",
    ProviderName: "Randall",
    mail: "randall@example.com",
    Subscription: "Standard",
    Amount: "$350",
    SubscriptionDurations: "1 Month",
    StartDate: "28 Nov 2023, 03:25 PM",
    EndDate: "28 Nov 2023, 03:25 PM",
  },
  {
    NUM: "6",
    img: "avatar-19.jpg",
    ProviderName: "Pricilla",
    mail: "pricilla@example.com",
    Subscription: "Basic",
    Amount: "$150",
    SubscriptionDurations: "3 Month",
    StartDate: "15 Nov 2023, 03:25 PM",
    EndDate: "18 Nov 2023, 03:25 PM",
  },
];
export default {
  data() {
    return {
      title: "Subscribers",
      data,
      columns,
    };
  },
};
</script>
