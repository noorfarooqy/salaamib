<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>

  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <element-breadcrumb :title="title" />
      <div class="row">
        <!-- Alert -->
        <div class="col-md-4">
          <div class="card">
            <div class="card-header">
              <div class="card-title">Alert</div>
            </div>
            <div class="card-body">
              <a
                @click="success"
                href="javascript: void(0);"
                class="btn btn-primary waves-effect waves-light"
                >Click me</a
              >
            </div>
          </div>
        </div>
        <!-- /Alert -->

        <!-- Alert -->
        <div class="col-md-4">
          <div class="card">
            <div class="card-header">
              <div class="card-title">Confirm</div>
            </div>
            <div class="card-body">
              <a
                @click="confirm"
                href="javascript: void(0);"
                id="alert-confirm"
                class="btn btn-primary waves-effect waves-light"
                >Click me</a
              >
            </div>
          </div>
        </div>
        <!-- /Alert -->

        <!-- Alert -->
        <div class="col-md-4">
          <div class="card">
            <div class="card-header">
              <div class="card-title">Prompt</div>
            </div>
            <div class="card-body">
              <a
                @click="prompt"
                href="javascript: void(0);"
                id="alert-prompt"
                class="btn btn-primary waves-effect waves-light"
                >Click me</a
              >
            </div>
          </div>
        </div>
        <!-- /Alert -->

        <!-- Alert -->
        <div class="col-md-4">
          <div class="card">
            <div class="card-header">
              <div class="card-title">Success Alert</div>
            </div>
            <div class="card-body">
              <a
                @click="openNotification()"
                href="javascript: void(0);"
                id="alert-success"
                class="btn btn-primary btn-sm waves-effect waves-light"
                >Click me</a
              >
            </div>
          </div>
        </div>
        <!-- /Alert -->

        <!-- Alert -->
        <div class="col-md-4">
          <div class="card">
            <div class="card-header">
              <div class="card-title">Error Alert</div>
            </div>
            <div class="card-body">
              <a
                @click="openNotificationerr()"
                href="javascript: void(0);"
                id="alert-error"
                class="btn btn-primary btn-sm waves-effect waves-light"
                >Click me</a
              >
            </div>
          </div>
        </div>
        <!-- /Alert -->

        <!-- Alert -->
        <div class="col-md-4">
          <div class="card">
            <div class="card-header">
              <div class="card-title">Warnng Alert</div>
            </div>
            <div class="card-body">
              <a
                @click="openNotificationwarr()"
                href="javascript: void(0);"
                id="alert-warning"
                class="btn btn-primary btn-sm waves-effect waves-light"
                >Click me</a
              >
            </div>
          </div>
        </div>
        <!-- /Alert -->
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
import { notification } from "ant-design-vue";
export default {
  data() {
    return {
      title: "Notification",
    };
  },
  // eslint-disable-next-line no-undef
  setup() {
    const openNotification = () => {
      notification.open({
        message: "Success message",
        placement: "bottomRight",
        bottom: "50px",
        duration: 3,
        style: {
          width: "250px",
          marginLeft: `${335 - 600}px`,
          background: "#2ab57d",
        },
      });
    };
    const openNotificationerr = () => {
      notification.open({
        message: "Error message",
        placement: "bottomRight",
        bottom: "50px",
        duration: 3,
        style: {
          width: "250px",
          marginLeft: `${335 - 600}px`,
          background: "#fd625e",
        },
      });
    };
    const openNotificationwarr = () => {
      notification.open({
        message: "Warning message",
        placement: "bottomRight",
        bottom: "50px",
        duration: 3,
        style: {
          width: "250px",
          marginLeft: `${335 - 600}px`,
          background: "#ffbf53",
        },
      });
    };
    return {
      openNotification,
      openNotificationerr,
      openNotificationwarr,
    };
  },
  methods: {
    success() {
      // eslint-disable-next-line no-undef
      Swal.fire({
        position: "top",
        title: "Alert Title",
        text: "Alert Message",
      }).then((result) => {
        if (result.isConfirmed) {
          notification.open({
            message: "Ok",
            placement: "bottomRight",
            bottom: "50px",
            duration: 3,
            style: {
              width: "250px",
              marginLeft: `${335 - 600}px`,
              background: "#2ab57d",
            },
          });
        }
      });
    },

    confirm() {
      // eslint-disable-next-line no-undef
      Swal.fire({
        position: "top",
        title: "AlertifyJS",
        text: "This is a confirm dialog.",
        confirmButtonColor: "#2fdf84",
        showCancelButton: true,
        cancelButtonText: "Cancel",
        confirmButtonText: "Confirm",
        // cancelButtonClasses: ["your-cancel-button-class"],
      }).then((result) => {
        if (result.isConfirmed) {
          notification.open({
            message: "Ok",
            placement: "bottomRight",
            bottom: "50px",
            duration: 3,
            style: {
              width: "250px",
              marginLeft: `${335 - 600}px`,
              background: "#2ab57d",
            },
          });
        } 
        // eslint-disable-next-line no-undef
        else if (result.dismiss === Swal.DismissReason.cancel) {
          notification.open({
            message: "Cancel",
            placement: "bottomRight",
            bottom: "50px",
            duration: 3,
            style: {
              width: "250px",
              marginLeft: `${335 - 600}px`,
              background: "#fd625e",
            },
          });
        }
      });
    },
    prompt() {
      // eslint-disable-next-line no-undef
      Swal.fire({
        position: "top",
        input: "text",
        confirmButtonText: "ok",
        showCancelButton: !0,
        confirmButtonClass: "btn btn-primary",
        buttonsStyling: !1,
        cancelButtonClass: "btn btn-danger ml-1",
      }).then((result) => {
        if (result.isConfirmed) {
          notification.open({
            message: "Ok:",
            placement: "bottomRight",
            bottom: "50px",
            duration: 3,
            style: {
              width: "250px",
              marginLeft: `${335 - 600}px`,
              background: "#2ab57d",
            },
          });
          // eslint-disable-next-line no-undef
        } else if (result.dismiss === Swal.DismissReason.cancel) {
          notification.open({
            message: "Cancel",
            placement: "bottomRight",
            bottom: "50px",
            duration: 3,
            style: {
              width: "250px",
              marginLeft: `${335 - 600}px`,
              background: "#fd625e",
            },
          });
        }
      });
    },
  },
};
</script>
<style>
.ant-notification-notice-closable .ant-notification-notice-message {
  color: white;
}

.ant-notification-close-x {
  display: none;
}
</style>
