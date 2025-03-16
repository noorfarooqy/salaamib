<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->

      <!-- /Page Header -->

      <div class="row">
        <div class="col-xl-3 col-md-4">
          <settingsidebar></settingsidebar>
        </div>
        <div class="col-xl-9 col-md-8">
          <div class="card">
            <div class="card-body w-100">
              <div class="content-page-header">
                <h5 class="setting-menu">Plan & Billing</h5>
              </div>
              <div class="owl-carousel" id="plan-billing-slider">
                <Carousel :wrap-around="true" :settings="settings" :breakpoints="breakpoints">
                  <Slide v-for="item in PlanBilling" :key="item.id">
                    <div class="owl-carousel-item">
                      <div :class="item.Class">
                        <div class="package-header d-sm-flex justify-content-between">
                          <div class="d-sm-flex">
                            <span class="icon-frame d-flex align-items-center justify-content-center"><img
                                :src="require(`@/assets/img/icons/${item.Image}`)" alt="img" /></span>
                            <div class="carousel-left">
                              <h5>
                                <a href="javascript:void(0);">{{ item.Title }}</a>
                              </h5>
                              <p>{{ item.Days }}</p>
                              <a href="javascript:void(0);" class="cancel-subscription">{{ item.Cancel }}</a>
                            </div>
                          </div>
                          <div>
                            <h5>{{ item.Rate }}</h5>
                            <p>{{ item.Total }}</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </Slide>
                  <template #addons>
                    <Pagination />
                  </template>
                </Carousel>
              </div>
              <!-- Search Filter -->
              <div class="row">
                <div class="col-sm-12">
                  <div class="card-table">
                    <div class="card-body">
                      <div class="table-responsive table-plan-billing">
                        <a-table class="stripped table-hover" :columns="columns" :data-source="data">
                          <template #bodyCell="{ column, record }">
                            <template v-if="column.key === 'Details'">
                              <td>
                                {{ record.Details }}
                                <p>{{ record.Details1 }}</p>
                              </td>
                            </template>

                            <template v-if="column.key === 'Download'">
                              <a class="btn-action-icon me-2" href="javascript:void(0);" download><i
                                  class="feather feather-download"></i></a>
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
        </div>
      </div>
    </div>
  </div>
</template>
<script>
const columns = [
  {
    title: "#",
    dataIndex: "id",
    sorter: {
      compare: (a, b) => {
        a = a.id.toLowerCase();
        b = b.id.toLowerCase();
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
    title: "Details",
    dataIndex: "Details",
    key: "Details",
    sorter: {
      compare: (a, b) => {
        a = a.Details.toLowerCase();
        b = b.Details.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Status",
    dataIndex: "Status",
    sorter: {
      compare: (a, b) => {
        a = a.Status.toLowerCase();
        b = b.Status.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Download",
    dataIndex: "Download",
    key: "Download",
    sorter: {
      compare: (a, b) => {
        a = a.Download.toLowerCase();
        b = b.Download.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
];
const data = [
  {
    id: "1",
    Date: "13 Aug 2023",
    Details: "ENTERPRISE",
    Details1: "lifetime",
    Status: "$199.99",
    Download: "",
  },
  {
    id: "2",
    Date: "13 Aug 2023",
    Details: "FREE TRAIL",
    Details1: "monthly",
    Status: "$0.00",
    Download: "",
  },
  {
    id: "3",
    Date: "13 Aug 2023",
    Details: "Basic",
    Details1: "Yearly",
    Status: "$49.99",
    Download: "",
  },
  {
    id: "4",
    Date: "13 Aug 2023",
    Details: "ENTERPRISE",
    Details1: "lifetime",
    Status: "$199.99",
    Download: "",
  },
];
import { Carousel, Pagination, Slide } from "vue3-carousel";
import "vue3-carousel/dist/carousel.css";
import PlanBilling from "@/assets/json/plan-billing.json";
export default {
  data() {
    return {
      data,
      columns,
      PlanBilling: PlanBilling,
      settings: {
        itemsToShow: 1,
        snapAlign: "center",
        loop: true,
        margin: 24,
      },

      breakpoints: {
        575: {
          itemsToShow: 1,
          snapAlign: "center",
        },
        // 700px and up
        767: {
          itemsToShow: 1,
          snapAlign: "center",
        },
        // 991px and up
        991: {
          itemsToShow: 2,
          snapAlign: "center",
        },
        // 1024 and up
        1024: {
          itemsToShow: 2,
          snapAlign: "start",
        },
      },
    };
  },
  components: {
    Carousel,
    Slide,
    Pagination,
  },
};
</script>
